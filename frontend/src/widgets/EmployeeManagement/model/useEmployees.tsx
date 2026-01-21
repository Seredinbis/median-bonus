import { useState, useEffect } from 'react';
import type { Employee, CreateEmployeeDto } from '@/shared/types/employee';

import { employeeApi } from '@/shared/api/employee';

export function useEmployees() {
  const [employees, setEmployees] = useState<Employee[]>([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  //ID должен браться из стора авторизации (например, Zustand или Redux)
  const currentBusinessId = "3fa85f64-5717-4562-b3fc-2c963f66afa6";

  const loadEmployees = async () => {
    try {
      const data = await employeeApi.getAll(currentBusinessId);
      setEmployees(data.employeees || []);
    } catch (e) {
      console.error("Ошибка загрузки:", e);
    }
  };

  const addEmployee = async (formData: Omit<CreateEmployeeDto, 'business_id'>) => {
    setIsLoading(true);
    try {
      await employeeApi.create({ ...formData, business_id: currentBusinessId });
      await loadEmployees();
      setIsModalOpen(false);
    } catch (e) {
      alert("Ошибка при создании пользователя");
    } finally {
      setIsLoading(false);
    }
  };

  const removeEmployee = async (id: string) => {
    if (!confirm('Вы уверены, что хотите удалить пользователя?')) return;
    try {
      await employeeApi.delete(id);
      setEmployees(prev => prev.filter(emp => emp.id !== id));
    } catch (e) {
      alert("Ошибка при удалении");
    }
  };

  useEffect(() => { loadEmployees(); }, []);

  return {
    employees,
    isModalOpen,
    isLoading,
    setIsModalOpen,
    addEmployee,
    removeEmployee
  };
}
