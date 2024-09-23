var hasAlert = false;

async function downloadSongs(url) {
  let result = await eel.startDownload(url)();
  console.log(result);

  let resultDiv = document.querySelector(".result");
  let alertDiv = document.createElement("div");

  if (result == 1) {
    alertDiv.classList.add("alert", "alert-success");
    alertDiv.textContent = "The songs have been downloaded successfully!";
  } else {
    alertDiv.classList.add("alert", "alert-danger");
    alertDiv.textContent = `An error occurred when trying to download the songs: ${result}`;
  }

  alertDiv.id = "alertMessage";
  resultDiv.appendChild(alertDiv);
  hasAlert = true;
}

function submitForm(e) {
  e.preventDefault();
  console.log(hasAlert);
  if (hasAlert) {
    let alertDiv = document.getElementById("alertMessage");
    if (alertDiv) {
      alertDiv.remove();
    }
  }

  let myform = document.getElementById("userInputForm");
  let formData = new FormData(myform);

  myform.reset();
  downloadSongs(formData.get("url"));
}

let myform = document.getElementById("userInputForm");
myform.addEventListener("submit", submitForm);
