import type { GetServerSideProps, NextPage } from "next";

interface Response {
  posts: string[];
}

const Home: NextPage<Response> = (context) => {
  return <div>{context.posts}</div>;
};

export default Home;

export const getServerSideProps: GetServerSideProps = async (context) => {
  return {
    props: [],
  };
};
