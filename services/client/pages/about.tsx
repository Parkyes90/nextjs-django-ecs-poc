import { NextPage } from "next";
import NavBar from "../components/NavBar";

const About: NextPage<Response> = (context) => {
  return (
    <div>
      <NavBar />
      About
    </div>
  );
};

export default About;
