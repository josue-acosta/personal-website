document.addEventListener('DOMContentLoaded', function () {
  // Side Nav for the moble menu
  var elems = document.querySelectorAll('.sidenav');
  var instances = M.Sidenav.init(elems, {});

  // Toast for the Send Email button
  var send_email_button = document.getElementById("send-email-button")
  send_email_button.addEventListener("click", MyMessage)

  function MyMessage() {
    M.toast({
      html: "Sending Email",
      classes: "rounded"
    });
  }
});
