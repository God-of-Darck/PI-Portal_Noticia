const $html = document.querySelector('html');
const $checkbox = document.getElementById('themingSwitcher');

// Verifica se já tem um tema salvo
const savedTheme = localStorage.getItem('theme');

// Aplica o tema salvo, se houver
if (savedTheme === 'dark') {
    $html.classList.add('dark-mode');
    $checkbox.checked = true; // Deixa o switch ativado
} else {
    $html.classList.remove('dark-mode');
    $checkbox.checked = false;
}

// Toda vez que o switch mudar, salva a escolha
$checkbox.addEventListener('change', function () {
    if (this.checked) {
        $html.classList.add('dark-mode');
        localStorage.setItem('theme', 'dark');
    } else {
        $html.classList.remove('dark-mode');
        localStorage.setItem('theme', 'light');
    }
});