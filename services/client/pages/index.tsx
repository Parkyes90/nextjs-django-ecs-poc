import type { GetServerSideProps, NextPage } from "next";
import NavBar from "../components/NavBar";
import axios from "axios";
import { UserList, UsersService } from "../generated";

axios.defaults.baseURL = process.env.BASE_API_URL;

type Props = {
  usersList: Array<UserList>;
};

const Home: NextPage<Props> = ({ usersList }) => {
  return (
    <div>
      <NavBar />
      <div> {usersList.map((user) => user.name)}</div>
    </div>
  );
};

export default Home;

export const getServerSideProps: GetServerSideProps = async (context) => {
  const usersList = await UsersService.usersList();
  return {
    props: { usersList }, // will be passed to the page component as props
  };
};
