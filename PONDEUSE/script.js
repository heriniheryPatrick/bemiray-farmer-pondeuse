// Initialisation du graphique de ponte
const ctx = document.getElementById('ponteChart').getContext('2d');
const ponteChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'],
        datasets: [{
            label: 'Taux de ponte (%)',
            data: [87, 88.2, 87.5, 89, 88, 88.5, 89.1],
            borderColor: '#27ae60',
            backgroundColor: 'rgba(39, 174, 96, 0.1)',
            borderWidth: 3,
            fill: true,
            tension: 0.3
        }]
    },
    options: {
        responsive: true,
        plugins: {
            legend: {
                display: false
            }
        },
        scales: {
            y: {
                min: 75,
                max: 100
            }
        }
    }
});

// Gestion du formulaire d'enregistrement rapide
document.getElementById('recordForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const date = document.getElementById('date').value;
    const eggs = document.getElementById('eggs').value;
    const mortality = document.getElementById('mortality').value;

    alert(`Données enregistrées pour le ${date} :\n- Œufs ramassés : ${eggs}\n- Mortalité : ${mortality}`);
    this.reset();
    document.getElementById('date').valueAsDate = new Date();
});

// Mettre la date du jour par défaut
document.getElementById('date').valueAsDate = new Date();