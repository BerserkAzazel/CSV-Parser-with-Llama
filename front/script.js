function calculateMean() {
  const fileInput = document.getElementById("fileInput");
  const columnNameInput = document.getElementById("columnNameInput");
  const resultContainer = document.getElementById("resultContainer");

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);
  formData.append("column_name", columnNameInput.value);

  fetch("/calculate_mean", {
    method: "POST",
    body: formData,
  })
    .then((response) => response.text())
    .then((result) => {
      resultContainer.innerHTML = `<p>${result}</p>`;
    })
    .catch((error) => {
      resultContainer.innerHTML = `<p>Error: ${error.message}</p>`;
    });
}
