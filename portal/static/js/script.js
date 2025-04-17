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

//Função para Pesquisar
document.getElementById("search-btn").addEventListener("click", function(){
    document.getElementById("search-form").onsubmit();
});


document.addEventListener("DOMContentLoaded", function () {
    const currentPath = window.location.pathname;
    const searchContainer = document.getElementById("search-container");

    // Oculta a barra de pesquisa somente na rota de uma notícia individual
    if (currentPath.startsWith("/noticia/") && searchContainer) {
        searchContainer.style.display = "none";
    }
});