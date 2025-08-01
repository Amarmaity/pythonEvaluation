function setupTableSearch(inputId, tableId, searchableColumns) {
    const input = document.getElementById(inputId);
    if (!input) return;

    input.addEventListener('keyup', function () {
        const searchValue = this.value.toLowerCase();
        const rows = document.querySelectorAll(`#${tableId} tbody tr`);

        rows.forEach(row => {
            const match = searchableColumns.some(index =>
                row.cells[index].textContent.toLowerCase().includes(searchValue)
            );
            row.style.display = match ? '' : 'none';
        });
    });
}
