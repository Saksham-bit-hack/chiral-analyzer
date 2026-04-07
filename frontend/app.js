// app.js - Frontend JavaScript application logic

// Molecule search function
async function searchMolecule(query) {
    const response = await fetch(`/api/search?query=${encodeURIComponent(query)}`);
    return await response.json();
}

// History management
let searchHistory = [];

function addToHistory(query) {
    searchHistory.push(query);
    localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
}

function loadHistory() {
    searchHistory = JSON.parse(localStorage.getItem('searchHistory')) || [];
}

// Display results
function displayResults(results) {
    const resultsContainer = document.getElementById('results');
    resultsContainer.innerHTML = '';
    results.forEach(result => {
        const item = document.createElement('div');
        item.textContent = result.name;
        resultsContainer.appendChild(item);
    });
}

// Main function to handle search
document.getElementById('searchButton').addEventListener('click', async () => {
    const query = document.getElementById('searchInput').value;
    const results = await searchMolecule(query);
    addToHistory(query);
    displayResults(results);
});

// Load history on startup
loadHistory();