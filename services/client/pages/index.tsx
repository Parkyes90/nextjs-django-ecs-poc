import type { GetServerSideProps, NextPage } from "next";

const Home: NextPage = () => {
  return <div>Testasdasdasasdzxcxcd</div>;
};

export default Home;

export const getServerSideProps: GetServerSideProps = async (context) => {
  return {
    props: {},
  };
};
