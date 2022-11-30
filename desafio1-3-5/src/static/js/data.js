$(document).ready(function(){
    $('#users').DataTable({
          "language": {
              "lengthMenu": "Mostrando _MENU_ registros por página",
              "zeroRecords": "Nada encontrado",
              "info": "Mostrando página _PAGE_ de _PAGES_",
              "infoEmpty": "Nenhum registro disponível",
              "infoFiltered": "(filtrado de _MAX_ registros no total)"
          }
      });
});

   $(document).ready(function() {
  $('#example').DataTable({
      "ajax": "data/objects.txt",
      "columns": [
          { "data": "email" },
          { "data": "assunto" },
          { "data": "descricao" }
    ]});
});
