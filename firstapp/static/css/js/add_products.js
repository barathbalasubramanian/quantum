

document.addEventListener('DOMContentLoaded', function() {

let formCount = 1; 
    document.getElementById('addMore').addEventListener('click', function() {
        const productFormSet = document.getElementById('productFormSet');

        const newForm = document.createElement('div');
        newForm.classList.add('productForm');

        const nameLabel = document.createElement('label');
        nameLabel.textContent = "Product Name:";
        newForm.appendChild(nameLabel);

        const nameInput = document.createElement('input');
        nameInput.type = 'text';
        nameInput.name = 'product_name_' + formCount;
        newForm.appendChild(nameInput);

        const priceLabel = document.createElement('label');
        priceLabel.textContent = "Price:";
        newForm.appendChild(priceLabel);

        const priceInput = document.createElement('input');
        priceInput.type = 'text';
        priceInput.name = 'product_price_' + formCount;
        newForm.appendChild(priceInput);

        productFormSet.appendChild(newForm);

        formCount++;
    })

});