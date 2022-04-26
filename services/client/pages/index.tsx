import type { GetServerSideProps, NextPage } from "next";

interface Response {
  posts: string[];
}

const Home: NextPage<Response> = (context) => {
  return <div>{context.posts}</div>;
};

export default Home;

export const getServerSideProps: GetServerSideProps = async (context) => {
  const res = await fetch("http://api:8000/posts");
  const data = await res.json();
  return {
    props: data,
  };
};
