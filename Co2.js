document.getElementById('carbonFootprintForm').addEventListener('submit', function(event) {
    event.preventDefault();

    // Constants for carbon emissions per activity (example values, not accurate)
    const emissions = {
        bodyType: {slim: 100, average: 120, obese: 150},
        sex: {male: 110, female: 100},
        diet: {vegan: 50, vegetarian: 70, meat: 100},
        showerFrequency: {daily: 30, everyOtherDay: 20, weekly: 10},
        heatingEnergySource: {gas: 500, electricity: 300},
        transport: {driving: 400, publicTransport: 200, cycling: 50},
        vehicleType: {gasoline: 300, electric: 100},
        socialActivity: {active: 50, moderate: 30, sedentary: 10},
        frequencyOfTravelingByAir: {frequent: 500, occasional: 300, rarely: 100},
        wasteBagSize: {small: 10, medium: 20, large: 30},
        energyEfficiency: {high: 50, medium: 100, low: 200},
        recycling: {yes: -50, no: 0},
        cookingWith: {electric: 50, gas: 100}
    };

    // Fetch values from form
    const bodyType = document.getElementById('bodyType').value;
    const sex = document.getElementById('sex').value;
    const diet = document.getElementById('diet').value;
    const showerFrequency = document.getElementById('showerFrequency').value;
    const heatingEnergySource = document.getElementById('heatingEnergySource').value;
    const transport = document.getElementById('transport').value;
    const vehicleType = document.getElementById('vehicleType').value;
    const socialActivity = document.getElementById('socialActivity').value;
    const monthlyGroceryBill = parseFloat(document.getElementById('monthlyGroceryBill').value);
    const frequencyOfTravelingByAir = document.getElementById('frequencyOfTravelingByAir').value;
    const vehicleMonthlyDistanceKm = parseFloat(document.getElementById('vehicleMonthlyDistanceKm').value);
    const wasteBagSize = document.getElementById('wasteBagSize').value;
    const wasteBagWeeklyCount = parseFloat(document.getElementById('wasteBagWeeklyCount').value);
    const tvPcHour = parseFloat(document.getElementById('tvPcHour').value);
    const newClothesMonthly = parseFloat(document.getElementById('newClothesMonthly').value);
    const internetDailyHour = parseFloat(document.getElementById('internetDailyHour').value);
    const energyEfficiency = document.getElementById('energyEfficiency').value;
    const recycling = document.getElementById('recycling').value;
    const cookingWith = document.getElementById('cookingWith').value;

    // Example calculations (very simplified)
    let totalEmission = 
        emissions.bodyType[bodyType] + 
        emissions.sex[sex] + 
        emissions.diet[diet] + 
        emissions.showerFrequency[showerFrequency] + 
        emissions.heatingEnergySource[heatingEnergySource] + 
        emissions.transport[transport] + 
        emissions.vehicleType[vehicleType] + 
        emissions.socialActivity[socialActivity] + 
        (monthlyGroceryBill * 0.1) + // Assuming 0.1 kg CO2e per dollar
        emissions.frequencyOfTravelingByAir[frequencyOfTravelingByAir] + 
        (vehicleMonthlyDistanceKm * 0.2) + // Assuming 0.2 kg CO2e per km for gasoline car
        (wasteBagWeeklyCount * emissions.wasteBagSize[wasteBagSize]) + 
        (tvPcHour * 5) + // Assuming 5 kg CO2e per hour for electronics
        (newClothesMonthly * 8) + // Assuming 8 kg CO2e per new clothing item
        (internetDailyHour * 1) + // Assuming 1 kg CO2e per hour for internet use
        emissions.energyEfficiency[energyEfficiency] + 
        emissions.recycling[recycling] + 
        emissions.cookingWith[cookingWith];

    // Display the result
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `Your estimated carbon footprint is: ${totalEmission} kg CO2e per month.`;

    // Optional: Redirect to results page with data
    // window.location.href = `results.html?footprint=${totalEmission}`;
});
