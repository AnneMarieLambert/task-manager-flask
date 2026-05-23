

document.addEventListener('DOMContentLoaded', () => {
    
    const flashAlerts = document.querySelectorAll('.alert');
    if (flashAlerts.length > 0) {
        flashAlerts.forEach(alert => {
            // Define que o alerta sumirá após 5 segundos
            setTimeout(() => {
                alert.style.transition = 'all 0.5s ease';
                alert.style.opacity = '0';
                alert.style.transform = 'translateY(-10px)';
                
                // Remove o elemento do DOM após a conclusão da transição
                setTimeout(() => {
                    alert.remove();
                }, 500);
            }, 5000);
        });
    }

    
    const deleteForms = document.querySelectorAll('form[action*="/task/delete/"]');
    deleteForms.forEach(form => {
        form.addEventListener('submit', (e) => {
            
            const confirmDelete = confirm('Tem certeza absoluta de que deseja excluir permanentemente esta tarefa? Esta ação é irreversível.');
            
            if (!confirmDelete) {
                
                e.preventDefault();
            }
        });
    });

    // 3. Efeito visual para arrastar/indicar interatividade nos cards
    const taskCards = document.querySelectorAll('.task-card');
    taskCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            
            card.style.transition = 'all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1)';
        });
    });
});
