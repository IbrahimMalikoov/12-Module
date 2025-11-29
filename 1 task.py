import random
import time


class HiringProcess:
    def __init__(self):
        self.vacancy_approved = False
        self.offer_accepted = False

    def log(self, actor, action):
        print(f"[{actor}]: {action}")
        time.sleep(0.5)  # Пауза для читаемости

    def run(self):
        print("=== НАЧАЛО ПРОЦЕССА НАЙМА ===\n")

        # --- 1. Подготовительный этап ---
        self.log("Руководитель", "Создает заявку на вакансию")

        while not self.vacancy_approved:
            self.log("HR-отдел", "Проверяет заявку...")
            if random.choice([True, False]):  # Симуляция решения
                self.vacancy_approved = True
                self.log("HR-отдел", "Заявка УТВЕРЖДЕНА")
            else:
                self.log("HR-отдел", "Заявка отклонена. Требуется доработка.")
                self.log("Руководитель", "Вносит правки в заявку")

        # --- 2. Этап отбора ---
        self.log("Система", "Вакансия опубликована на сайте")
        self.log("Кандидат", "Подает заявку (резюме)")

        self.log("HR-отдел", "Проверяет анкету кандидата...")
        # Ветвление: Анкета подходит?
        if not self.decision_gate("Анкета соответствует требованиям?"):
            self.send_rejection("Несоответствие резюме")
            return

        # --- 3. Этап собеседования ---
        self.log("HR-отдел", "Приглашает на первичное интервью")

        # Ветвление: Первичное интервью
        if not self.decision_gate("Первичное интервью пройдено?"):
            self.send_rejection("Не прошел HR-скрининг")
            return

        self.log("Руководитель", "Проводит техническое собеседование")

        # Ветвление: Техническое интервью
        if not self.decision_gate("Техническое интервью пройдено?"):
            self.send_rejection("Не хватило технических навыков")
            return

        # --- 4. Заключительный этап (Оффер) ---
        self.log("HR-отдел", "Отправляет оффер кандидату")

        # Ветвление: Решение кандидата
        if not self.decision_gate("Кандидат принял оффер?"):
            self.send_rejection("Кандидат отказался от предложения")
            return

        # --- Параллельные действия (Fork/Join) ---
        print("\n--- FORK (Параллельные процессы) ---")
        self.parallel_onboarding()
        print("--- JOIN (Слияние процессов) ---\n")

        self.log("Процесс", "Успешно завершен. Сотрудник нанят.")
        print("\n=== КОНЕЦ ===")

    def decision_gate(self, question):
        """Симуляция принятия решения (Да/Нет)"""
        result = random.choice([True, False])  # 50/50 шанс
        # Для демонстрации можно раскомментировать строку ниже, чтобы всегда было "Да"
        # result = True
        print(f"   >>> {question} {'ДА' if result else 'НЕТ'}")
        return result

    def send_rejection(self, reason):
        self.log("Система", f"Отправляет уведомление об отказе. Причина: {reason}")
        print("\n=== КОНЕЦ (Отказ) ===")

    def parallel_onboarding(self):
        # В реальном коде здесь были бы асинхронные задачи или потоки
        task1 = "Система добавляет сотрудника в БД"
        task2 = "IT-отдел настраивает рабочее место"

        self.log("Система", "Начинает регистрацию...")
        self.log("IT-отдел", "Получает заявку на оборудование...")

        # Симуляция выполнения
        self.log("Система", "Готово: Сотрудник в базе (ID: 101)")
        self.log("IT-отдел", "Готово: Ноутбук и доступы выданы")


# Запуск
if __name__ == "__main__":
    process = HiringProcess()
    process.run()