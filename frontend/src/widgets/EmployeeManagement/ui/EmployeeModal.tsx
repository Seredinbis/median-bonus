import { useState } from 'react';
import { Modal } from '@/shared/ui/Modal/Modal';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  onSave: (data: any) => void;
  loading: boolean;
}

export const EmployeeModal = ({ isOpen, onClose, onSave, loading }: Props) => {
  const [form, setForm] = useState({ name: '', email: '', password: '' });

  return (
    <Modal isOpen={isOpen} onClose={onClose} title="Добавить сотрудника">
      <div className="space-y-4">
        {/* Поле ФИО */}
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-gray-400 ml-1">ФИО сотрудника</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 transition-all"
            placeholder="Иван Иванов"
            value={form.name}
            onChange={e => setForm({...form, name: e.target.value})}
          />
        </div>

        {/* Поле Email */}
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-gray-400 ml-1">Электронная почта</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 transition-all"
            placeholder="example@mail.com"
            type="email"
            value={form.email}
            onChange={e => setForm({...form, email: e.target.value})}
          />
        </div>

        {/* Поле Пароль */}
        <div className="space-y-1.5">
          <label className="text-sm font-medium text-gray-400 ml-1">Пароль</label>
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 focus:ring-1 focus:ring-orange-500 transition-all"
            placeholder="••••••••"
            type="password"
            value={form.password}
            onChange={e => setForm({...form, password: e.target.value})}
          />
        </div>
      </div>

      <div className="flex flex-col gap-3 mt-8">
        <button
          onClick={() => onSave(form)}
          disabled={loading || !form.email || !form.password}
          className="w-full bg-orange-500 hover:bg-orange-600 py-3 rounded-xl text-white font-bold disabled:opacity-50 transition-all active:scale-[0.98]"
        >
          {loading ? 'Создание...' : 'Создать'}
        </button>
        <button onClick={onClose} className="w-full text-gray-500 hover:text-white py-2 transition-colors text-sm">
          Отмена
        </button>
      </div>
    </Modal>
  );
};
