// Dark mode toggle based on session
window.addEventListener('DOMContentLoaded', function() {
	fetch('/api-darkmode-status')
		.then(res => res.json())
		.then(data => {
			if (data.darkmode) {
				document.body.classList.remove('lightmode');
			} else {
				document.body.classList.add('lightmode');
			}
		});
});


