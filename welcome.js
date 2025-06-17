function showLoginPage() {
    // Hide Welcome Page and show Login Page
    document.getElementById('welcomePage').classList.add('hidden');
    window.location.href = 'login.html';  // Redirect to Login Page
}