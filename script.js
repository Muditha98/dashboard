// Company data
const companies = [
    {
        name: 'Microsoft',
        marketCap: '3.1T',
        revenue: '211.9B',
        growth: 15.2,
        employees: 221000
    },
    {
        name: 'Apple',
        marketCap: '2.8T',
        revenue: '383.9B',
        growth: 7.8,
        employees: 164000
    },
    {
        name: 'Google',
        marketCap: '1.7T',
        revenue: '282.8B',
        growth: 9.8,
        employees: 156000
    },
    {
        name: 'Amazon',
        marketCap: '1.6T',
        revenue: '513.9B',
        growth: 11.2,
        employees: 1608000
    },
    {
        name: 'Meta',
        marketCap: '1.2T',
        revenue: '134.9B',
        growth: 16.5,
        employees: 66000
    }
];

// Add hover effects and click handlers
document.querySelectorAll('.company-card').forEach((card, index) => {
    const company = companies[index];
    
    // Add additional info on hover
    card.addEventListener('mouseenter', () => {
        const metrics = card.querySelector('.metrics');
        
        // Check if we already added the additional metrics
        if (!card.querySelector('.additional-metrics')) {
            const additionalMetrics = document.createElement('div');
            additionalMetrics.className = 'additional-metrics';
            additionalMetrics.innerHTML = `
                <div class="metric">
                    <span class="label">Growth</span>
                    <span class="value">+${company.growth}%</span>
                </div>
                <div class="metric">
                    <span class="label">Employees</span>
                    <span class="value">${company.employees.toLocaleString()}</span>
                </div>
            `;
            metrics.appendChild(additionalMetrics);
        }
    });

    // Remove additional info on mouse leave
    card.addEventListener('mouseleave', () => {
        const additionalMetrics = card.querySelector('.additional-metrics');
        if (additionalMetrics) {
            additionalMetrics.remove();
        }
    });

    // Add click animation
    card.addEventListener('click', () => {
        card.style.transform = 'scale(0.95)';
        setTimeout(() => {
            card.style.transform = '';
        }, 100);
    });
});