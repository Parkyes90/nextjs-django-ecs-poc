import type { GetServerSideProps, NextPage } from "next";

const Home: NextPage = () => {
  return <div>Test</div>;
};

export default Home;

export const getServerSideProps: GetServerSideProps = async (context) => {
  return {
    props: {},
  };
};
