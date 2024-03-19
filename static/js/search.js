const SearchApp = {
    data() {
        return {
            query: '',
            company_size: '',
            jobs: []
        }
    },
    methods: {
        performSearch() {
            if (!this.query) {
                alert('Please enter a search query.');
                return;
            }

            var data = {
                'query': this.query,
                'company_size': this.company_size
            }

            fetch('/api/search/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                body: JSON.stringify(data)
            })
            .then((response) => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.json()
            })
            .then((result) => {
                console.log('Success', result.jobs);
                this.jobs = result.jobs
            })
            .catch((error) => {
                console.error('Error', error);
                alert('An error occurred while performing the search.');
            });
        }
    }
};

Vue.createApp(SearchApp).mount('#search-app');

// Function to get CSRF token from cookie
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}