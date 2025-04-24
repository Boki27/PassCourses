import { useQuery } from "@tanstack/react-query";
import axios from "axios";

interface Posts {
  id: number;
  title: string;
  userId: number;
  completed: boolean;
}

interface PostQuery {
  page: number;
  pageSize: number;
}

const usePosts = (query: PostQuery) => {
  const fecthPosts = () =>
    axios
      .get<Posts[]>("https://jsonplaceholder.typicode.com/posts", {
        params: {
          _start: (query.page - 1) * query.pageSize,
          _limit: query.pageSize,
        },
      })
      .then((res) => res.data);

  return useQuery<Posts[], Error>({
    queryKey: ["posts", query],
    queryFn: fecthPosts,
    staleTime: 10 * 1000,
    keepPreviousData: true,
  });
};

export default usePosts;
