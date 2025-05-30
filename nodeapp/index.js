
const express = require('express');
const NodeCache = require('node-cache');
const app = express();
const cache = new NodeCache({ stdTTL: 10 });

app.get('/ping', (req, res) => res.send('Aplicação Node.js viva!'));

app.get('/time', (req, res) => {
  const cached = cache.get('time');
  if (cached) return res.send(cached);

  const time = new Date().toISOString();
  cache.set('time', time);
  res.send(time);
});

app.listen(3000, () => console.log('App Node.js rodando na porta 3000'));
