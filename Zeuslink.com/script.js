// Code to handle navigation buttons
const homeButton = document.querySelector('a[href="index.html"]');
const aboutButton = document.querySelector('a[href="about.html"]');
const ledgerButton = document.querySelector('a[href="ledger.html"]');

homeButton.addEventListener('click', () => {
  // Code to show home page
});

aboutButton.addEventListener('click', (event) => {
  event.preventDefault(); // prevent the default behavior of the link
  window.location.href = "about.html"; // navigate to the about.html file
});

ledgerButton.addEventListener('click', () => {
  // Code to show ledger page
});
