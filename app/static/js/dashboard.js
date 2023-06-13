function fetchData() {
  // Fetch data from the server
  fetch('/get_expenditures_by_category')
    .then((response) => response.json())
    .then((data) => {
      const labels = [];
      const expenditures = [];

      // Populate label and expenditure arrays
      for (const category in data) {
        labels.push(category);
        expenditures.push(data[category]);
      }

      // Create a new pie chart
      const ctx = document.getElementById('expenditureChart').getContext('2d');
      new Chart(ctx, {
        type: 'pie',
        data: {
          labels: labels,
          datasets: [{
            data: expenditures,
            backgroundColor: ['rgba(255, 99, 132, 0.8)', 'rgba(54, 162, 235, 0.8)', 'rgba(255, 206, 86, 0.8)', 'rgba(75, 192, 192, 0.8)', 'rgba(153, 102, 255, 0.8)'],
          }],
        },
      });
    })
    .catch((error) => console.error(error));
}

// Call fetchData() to fetch and render the data
fetchData();
