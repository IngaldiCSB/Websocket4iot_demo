var WebSocketServer = require('websocket').server;
var http = require('http');
 
var server = http.createServer(function(request, response) {
    // Qui possiamo processare la richiesta HTTP
    // Dal momento che ci interessano solo le WebSocket, non dobbiamo implementare nulla
});
server.listen(3000, function() {

   console.log("server in ascolto")

 });
 
// Creazione del server
wsServer = new WebSocketServer({
    httpServer: server
});
 
// Gestione degli eventi
wsServer.on('request', function(request) {
    var connection = request.accept(null, request.origin);
 
    console.log("connessione accettata")
    setInterval(function(){connection.sendUTF("Stringa di esempio")} , 1000);

    connection.on('message', function(message) {
        // Metodo eseguito alla ricezione di un messaggio
        if (message.type === 'utf8') {
            // Se il messaggio è una stringa, possiamo leggerlo come segue:
            console.log('Il messaggio ricevuto è: ' + message.utf8Data);
        }
    });
 
    connection.on('close', function(connection) {
        // Metodo eseguito alla chiusura della connessione
    });
});
