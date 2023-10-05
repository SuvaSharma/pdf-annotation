// let pdfDoc = null;
// let pdfPageNumber = 1;
// let pdfCanvas = document.getElementById('pdf-canvas');
// let penButton = document.getElementById('pen-button');
// let penColor = document.getElementById('pen-color');
// let penThickness = document.getElementById('pen-thickness');
// let saveButton = document.getElementById('save-button');
// let ctx = pdfCanvas.getContext('2d');
// let drawing = false;
// let lastX = 0;
// let lastY = 0;


// document.addEventListener('DOMContentLoaded', function () {
//   loadPdf();
// });


// function loadPdf() {
//   let pdfPath = '{% url "view_pdf" pdf_file.pk %}?page=' + pdfPageNumber;
//   pdfjsLib.getDocument(pdfPath).promise.then(function (pdf) {
//     pdfDoc = pdf;
//     renderPage(pdfPageNumber);
//   });
// }

// // Render a specific page
// function renderPage(pageNumber) {
//   pdfDoc.getPage(pageNumber).then(function (page) {
//     let viewport = page.getViewport({ scale: 1.5 });
//     pdfCanvas.height = viewport.height;
//     pdfCanvas.width = viewport.width;

//     let renderContext = {
//       canvasContext: ctx,
//       viewport: viewport,
//     };

//     page.render(renderContext);
//   });
// }


// pdfCanvas.addEventListener('mousedown', startDrawing);
// pdfCanvas.addEventListener('mousemove', draw);
// pdfCanvas.addEventListener('mouseup', stopDrawing);
// pdfCanvas.addEventListener('mouseout', stopDrawing);

// function startDrawing(e) {
//   drawing = true;
//   [lastX, lastY] = [e.offsetX, e.offsetY];
//   ctx.strokeStyle = penColor.value;
//   ctx.lineWidth = penThickness.value;
//   ctx.lineJoin = 'round';
//   ctx.lineCap = 'round';
//   ctx.beginPath();
//   ctx.moveTo(lastX, lastY);
// }

// function draw(e) {
//   if (!drawing) return;
//   ctx.lineTo(e.offsetX, e.offsetY);
//   ctx.stroke();
//   [lastX, lastY] = [e.offsetX, e.offsetY];
// }

// function stopDrawing() {
//   drawing = false;
//   ctx.closePath();
// }



// saveButton.addEventListener('click', saveAnnotations);

// function saveAnnotations() {
//   let canvasDataURL = pdfCanvas.toDataURL('image/png');
//   let annotations = {
//   page: pdfPageNumber,
//   dataURL: canvasDataURL,
//  };
// }