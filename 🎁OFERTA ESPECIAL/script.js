// --- ATENÇÃO: EM UM PROJETO REAL E SEGURO, SENHAS NUNCA DEVEM ESTAR NO CÓDIGO FRONT-END! ---
// Este código é APENAS PARA FINS DEMONSTRATIVOS E EDUCACIONAIS.
// Para um sistema real, você precisaria de um servidor (backend) para armazenar e validar senhas de forma segura (hashing).

// Múltiplas senhas válidas para acesso ao Guia
const SENHAS_SECRETAS_VALIDAS = [
    "123",
    "descoberta",
    "aventura",
    "conhecimento",
    "geniomestre" // Adicionei mais uma senha aqui!
];

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Impede o envio padrão do formulário

    const passwordInput = document.getElementById('password').value.trim(); // Pega a senha e remove espaços
    const errorMessage = document.getElementById('errorMessage');

    errorMessage.textContent = ''; // Limpa mensagens de erro anteriores

    // Verifica se a senha digitada está na lista de senhas secretas válidas
    if (SENHAS_SECRETAS_VALIDAS.includes(passwordInput)) {
        // Se a senha for válida, redireciona para a página de destino
        window.location.href = "curso.html"; // Mantenha o nome do arquivo HTML de destino
    } else {
        errorMessage.textContent = "Senha Secreta inválida. Tente novamente!";
    }
});