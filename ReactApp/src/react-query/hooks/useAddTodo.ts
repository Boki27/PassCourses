import { useMutation, useQueryClient } from "@tanstack/react-query";
import { CACHE_KEY_TODOS } from "../constants";
import todoService, { Todo } from "../services/todoService";

const useAddTodo = (p0: () => void) => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: todoService.post,

    onSuccess: (savedTodo, newTodo) => {
      // aproach: Invalidating the cache
      // queryClient.invalidateQueries({
      //   queryKey: ["todos"],
      // });
      // aproach 2: updating data in the cache directly
      queryClient.setQueryData<Todo[]>(CACHE_KEY_TODOS, (todos = []) => [
        savedTodo,
        ...todos,
      ]);
    },
  });
};

export default useAddTodo;
