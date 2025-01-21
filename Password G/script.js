// Toggle Dark/Light Mode
document.getElementById('theme-toggle').addEventListener('click', toggleTheme);

function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    const currentTheme = document.body.classList.contains('dark-mode') ? '🌙' : '🌞';
    document.getElementById('theme-toggle').textContent = currentTheme;
}

// Generate Password
document.getElementById('generate-btn').addEventListener('click', generatePassword);
document.getElementById('copy-btn').addEventListener('click', copyPassword);

function generatePassword() {
    const length = parseInt(document.getElementById('length').value);
    const includeUppercase = document.getElementById('uppercase').checked;
    const includeLowercase = document.getElementById('lowercase').checked;
    const includeNumbers = document.getElementById('numbers').checked;
    const includeSpecial = document.getElementById('special').checked;

    let charset = '';
    if (includeUppercase) charset += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    if (includeLowercase) charset += 'abcdefghijklmnopqrstuvwxyz';
    if (includeNumbers) charset += '0123456789';
    if (includeSpecial) charset += '!@#$%^&*()_-+=<>?';

    let password = '';
    for (let i = 0; i < length; i++) {
        password += charset.charAt(Math.floor(Math.random() * charset.length));
    }

    document.getElementById('password').value = password;
}

function copyPassword() {
    const passwordField = document.getElementById('password');
    passwordField.select();
    passwordField.setSelectionRange(0, 99999); // For mobile devices
    document.execCommand('copy');
    alert('Password copied to clipboard!');
}
