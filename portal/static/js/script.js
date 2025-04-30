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
    const path = window.location.pathname;
    const searchContainer = document.getElementById("search-container");

    const pathsToHideSearch = [
        "/noticia/",
        "/sobrenos",
        "/politicas",
        "/ia",
        "/ti",
        "/games",
        "/robotica"
    ];

    if (pathsToHideSearch.some(p => path.startsWith(p))) {
        if (searchContainer) {
            searchContainer.style.display = "none";
        }
    }
});

// /* Função para rolar os cards dentro do carrossel */
// function scrollCards(id, direction) {
//     const wrapper = document.getElementById(id);
//     const scrollAmount = wrapper.offsetWidth / 2;
//     wrapper.scrollBy({ left: direction * scrollAmount, behavior: 'smooth' });
//   }
// /* Função para rolar os cards dentro do carrossel */
// function scrollCards(wrapperId, direction) {
//     const wrapper = document.getElementById(wrapperId); /* Seleciona o contêiner dos cards */
//     const scrollAmount = 320; /* Quantidade de pixels a ser rolada por vez (ajustável) */
    
//     /* Rola os cards para a esquerda ou direita */
//     wrapper.scrollBy({
//       left: direction * scrollAmount, /* Rola para a direção escolhida (esquerda ou direita) */
//       behavior: 'smooth' /* Aplica animação suave */
//     });
//   }