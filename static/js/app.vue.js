var app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        band: {},
        albums: {}
    },
    methods: {
        fetchData: function() {
            this.$http.get('/testband').then(response => {
              this.band = response.body;
            }, response => {
                console.log("an error occurred");
            }).then(() => { 
                this.$http.post('/testalbums', {params: {'band': this.band['title']}}).then(response => {
                  this.albums = response.body;
                }, response => {
                    console.log("an error occurred");
                });
              }
            )
        }
    },
    mounted: function() {
        this.fetchData();
    }
})