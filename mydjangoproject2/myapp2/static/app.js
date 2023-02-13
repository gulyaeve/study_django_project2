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

function onDragStart(event) {
event
    .dataTransfer
    .setData('text/plain', event.target.id);

  event
    .currentTarget
    .style
    .backgroundColor = 'red';
}
function onDragOver(event) {
  event.preventDefault();
}
function onDrop(event) {
  const id = event
    .dataTransfer
    .getData('text');
const draggableElement = document.getElementById(id);
const dropzone = event.target;
dropzone.appendChild(draggableElement);
  event
    .dataTransfer
    .clearData(); }