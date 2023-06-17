<script>
    document.addEventListener('DOMContentLoaded', function() {
        var form = document.querySelector('form');
        var resultadoCard = document.getElementById('resultado-card');

        form.addEventListener('submit', function(e) {
            e.preventDefault();

            fetch(form.action, {
                method: 'POST',
                body: new FormData(form),
            })
            .then(function(response) {
                return response.text();
            })
            .then(function(result) {
                resultadoCard.style.display = 'block';
            })
            .catch(function(error) {
                console.log('Error:', error);
            });
        });
    });
</script>
