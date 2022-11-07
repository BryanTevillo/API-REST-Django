import React, { Component } from "react";
import DummyData from "./dummydata.json";
import PizzaDetail from "./pizzeriasdetail";
import axios from "axios";

export class PizzaList extends Component {
  componentDidMount() {
    axios
      .get("http://127.0.0.1:8000/")
      .then((respuesta) => {
        console.log(respuesta);
      })
      .catch(function (error) {
        console.log(error);
      });
  }
  render() {
    return (
      <div>
        {DummyData.map((item) => (
          <PizzaDetail p={item} />
        ))}
      </div>
    );
  }
}

export default PizzaList;
