
const express = require("express");
const app = express();
const PORT = 8000;
const { faker } = require('@faker-js/faker');

// ***MIDDLEWRAE***
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const createUser = () => {
    const newUser = {
        password: faker.internet.password(),
        email: faker.internet.email({ firstName, lastName }),
        phoneNumber: faker.phone.number(),
        lastName: faker.person.lastName(),
        firstName: faker.person.firstName(sex),
        _id: faker.database.mongodbObjectId(),



    };
    return newUser;
};

const createCompany = () => {
    const newCompany = {
        _id: faker.database.mongodbObjectId(),
        name: faker.company.name(),
        address: { 
            street: faker.location.streetAddress(), 
            city :faker.location.city(),
            zipCode:faker.location.zipCode(),
            state :faker.location.state(),
            country:faker.location.country(),
        },
    };
    return newFake;
};
app.post("/api/users/new", (req, res) => {
  console.log(req.body);
  users.push(req.body);
  res.json(users);
});
app.post("/api/companies/new", (req, res) => {
  console.log(req.body);
  users.push(req.body);
  res.json(companies);
});
app.post("/api/user/company", (req, res) => {
    console.log(req.body);
    users.push(req.body);
    res.json(user);
  });
app.listen(PORT, () => {
  console.log(`The server is up & running on PORT ${PORT}`);
});




