const amountInput = document.getElementById('amountInput');

const currencySelect = document.getElementById('currencySelect');

const convertButton = document.getElementById('convertButton');

const result = document.getElementById('result');



// Mock exchange rates

const exchangeRates = {

    USD: 1.2,

    EUR: 1.1

};



convertButton.addEventListener('click', function() {

    try {

        const amount = parseFloat(amountInput.value);

        if (isNaN(amount) || amount <= 0) {

            throw new Error('Invalid amount. Please enter a positive number.');

        }



        const currency = currencySelect.value;

        if (!exchangeRates[currency]) {

            throw new Error('Unsupported currency selected.');

        }



        // Perform conversion

        const convertedAmount = (amount * exchangeRates[currency]).toFixed(2);

        result.textContent = `Converted Amount: ${convertedAmount} ${currency}`;

    } catch (error) {

        result.textContent = `Error: ${error.message}`;

    } finally {

        // Clean up input

        amountInput.value = '';

    }

});