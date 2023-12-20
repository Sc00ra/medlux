document.addEventListener('DOMContentLoaded', function() {
    updateDateTime();

    // Update date and time every second
    setInterval(updateDateTime, 1000);
});

function updateDateTime() {
    const datetimeElement = document.getElementById('datetime');
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric', hour12: false };
    const formattedDateTime = now.toLocaleString('pl-PL', options);
    datetimeElement.textContent = formattedDateTime;
}
