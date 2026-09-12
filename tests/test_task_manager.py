import json
import os
import tempfile
import unittest

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def test_add_task_returns_the_created_task_and_increments_id(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, "tasks.json")
            manager = TaskManager(file_path)

            task = manager.add_task("Primera tarea")

            self.assertEqual(task.id, 1)
            self.assertEqual(task.description, "Primera tarea")
            self.assertEqual(manager._next_id, 2)

    def test_invalid_json_file_is_handled_gracefully(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, "tasks.json")
            with open(file_path, "w", encoding="utf-8") as handle:
                handle.write("{not valid json}")

            manager = TaskManager(file_path)

            self.assertEqual(manager._tasks, [])
            self.assertEqual(manager._next_id, 1)

    def test_complete_task_accepts_string_ids(self):
        with tempfile.TemporaryDirectory() as tmp_dir:
            file_path = os.path.join(tmp_dir, "tasks.json")
            with open(file_path, "w", encoding="utf-8") as handle:
                json.dump([{"id": 1, "description": "Tarea", "completed": False}], handle)

            manager = TaskManager(file_path)

            result = manager.complete_task("1")

            self.assertIsNotNone(result)
            self.assertTrue(result.completed)
            self.assertTrue(manager._tasks[0].completed)

    def test_simulated_tasks_are_loaded_without_reading_json_file(self):
        manager = TaskManager(initial_tasks=[
            {"id": 10, "description": "Tarea simulada", "completed": False},
            {"id": 11, "description": "Otra tarea", "completed": True},
        ])

        self.assertEqual(len(manager._tasks), 2)
        self.assertEqual(manager._next_id, 12)
        self.assertEqual(manager._tasks[0].description, "Tarea simulada")


if __name__ == "__main__":
    unittest.main()
