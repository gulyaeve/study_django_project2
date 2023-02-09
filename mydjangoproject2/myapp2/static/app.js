new Vue({
    el: '#players_data',
    data:{
    players: []
    },
    created: function(){
        const vm = this;
        axios.get('/api/players/')
        .then(function(response){
//        console.log(response.data)
        vm.players = response.data

        })
    }
}
)