fetch('/expenses_by_category')
  .then(response => response.json())
  .then(data => {
    // `data` is the JSON data returned by the server
    // You can use this data to update your chart
  });


let myChart = new Chart(document.getElementById('myChart'), {
type: 'pie',  // or 'bar', 'line', etc.
data: {
    labels: [],  // Categories
    datasets: [{
    data: [],  // Expenses
    // ...other options...
    }]
},
// ...other options...
});
  
document.getElementById('expenseForm').addEventListener('submit', event => {
    // Prevent the form from being submitted normally
    event.preventDefault();
  
    // Fetch the updated data and update the chart
    fetch('/expenses_by_category')
      .then(response => response.json())
      .then(data => {
        myChart.data.labels = Object.keys(data);
        myChart.data.datasets[0].data = Object.values(data);
        myChart.update();
      });
  });
  