
const Joke = require("../models/joke");

module.exports.findAllJokes = (req, res) => {
  Joke.find()
    .then((jokes) => {
      res.json(jokes);
    })
    .catch((err) => res.json(err));
};


module.exports.findOneJoke = (req, res) => {
  Joke.findOne({ _id: req.params.id })
    .then((oneJoke) => {
      res.json(oneJoke);
    })
    .catch((err) => res.json(err));
};



module.exports.createNewJoke = (req, res) => {
  Joke.create(req.body)
    .then((newlyCreatedJoke) => {
      res.json(newlyCreatedJoke);
    })
    .catch((err) => res.json(err));
};



module.exports.updateExisitingJoke = (req, res) => {
  Joke.findOneAndUpdate({ _id: req.params.id }, req.body, {
    new: true,
    runValidators: true,
  })
    .then((updatedJoke) => {
      res.json(updatedJoke);
    })
    .catch((err) => res.json(err));
};


module.exports.deleteOneJoke = (req, res) => {
  Joke.deleteOne({ _id: req.params.id })
    .then((result) => {
      res.json(result);
    })
    .catch((err) => res.json(err));
};