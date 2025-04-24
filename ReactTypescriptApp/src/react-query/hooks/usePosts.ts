import { useQuery } from "@tanstack/react-query";
import axios from "axios";

interface Posts {
  id: number;
  title: string;
  userId: number;
  completed: boolean;
}

const usePosts = (userId: number | undefined) => {
  const fecthPosts = () =>
    axios
      .get<Posts[]>("https://jsonplaceholder.typicode.com/posts", {
        params: {
          userId,
        },
      })
      .then((res) => res.data);

  return useQuery<Posts[], Error>({
    queryKey: userId ? ["users", userId, "posts"] : ["posts"],
    queryFn: fecthPosts,
    staleTime: 10 * 1000,
  });
};

export default usePosts;
