// pdf_annotation.js
const pdfUrl = '{% url "view_pdf" pdf_file.id %}';
const canvas = document.getElementById('pdf-container');
const saveButton = document.getElementById('save-annotations');
const annotationsTextarea = document.getElementById('annotations');

let pdfDoc = null;
let pdfPageNumber = 1;

// Initialize PDF.js
pdfjsLib.getDocument(pdfUrl).promise.then(function(doc) {
  pdfDoc = doc;
  renderPage(pdfPageNumber);
});

function renderPage(pageNumber) {
  pdfDoc.getPage(pageNumber).then(function(page) {
    const scale = 1.5;
    const viewport = page.getViewport({ scale });

    // Prepare canvas using PDF page dimensions
    const canvasElement = document.createElement('canvas');
    const context = canvasElement.getContext('2d');
    canvasElement.height = viewport.height;
    canvasElement.width = viewport.width;

    // Append canvas to the container
    canvas.innerHTML = ''; // Clear previous canvas
    canvas.appendChild(canvasElement);

    // Render PDF page into canvas
    const renderContext = {
      canvasContext: context,
      viewport: viewport,
    };
    page.render(renderContext);
  });
}

// Add event listener for saving annotations
saveButton.addEventListener('click', function() {
  const annotations = annotationsTextarea.value;

  // Update the annotations in the database via AJAX
  const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

  fetch('{% url "edit_pdf" pdf_file.id %}', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrfToken,
    },
    body: JSON.stringify({ annotations: annotations }),
  })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        alert('Annotations saved successfully.');
      } else {
        alert('Failed to save annotations.');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      alert('An error occurred while saving annotations.');
    });
});
