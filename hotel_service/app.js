const express = require('express');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());

const reservas = [];

// Simular falla aleatoria
function fallaAleatoria(probabilidad = 0.3) {
  return Math.random() < probabilidad;
}

app.post('/reserve', (req, res) => {
  const user = req.body.user;

  if (fallaAleatoria()) {
    return res.status(500).json({ message: `Error al reservar hotel para ${user}` });
  }

  reservas.push(user);
  res.status(200).json({ message: `Hotel reservado para ${user}` });
});

app.post('/cancel', (req, res) => {
  const user = req.body.user;
  const index = reservas.indexOf(user);
  if (index !== -1) {
    reservas.splice(index, 1);
    res.status(200).json({ message: `Reserva de hotel cancelada para ${user}` });
  } else {
    res.status(404).json({ message: `No hay reserva de hotel para ${user}` });
  }
});

app.get('/reservas', (req, res) => {
  res.status(200).json(reservas);
});

app.listen(5002, () => {
  console.log('Hotel Service listening on port 5002');
});
