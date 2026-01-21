import { useState } from 'react';

interface Props {
  isOpen: boolean;
  onClose: () => void;
  onSave: (data: any) => void;
  loading: boolean;
}

export const EmployeeModal = ({ isOpen, onClose, onSave, loading }: Props) => {
  const [form, setForm] = useState({ name: '', email: '', password: '' });

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-black/80 backdrop-blur-sm flex items-center justify-center z-50 p-4">
      <div className="bg-[#1E1E1E] border border-gray-800 p-6 rounded-2xl w-full max-w-md shadow-2xl">
        <h2 className="text-xl font-bold mb-6 text-white text-center">Добавить пользователя</h2>

        <div className="space-y-4">
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-colors"
            placeholder="ФИО"
            value={form.name}
            onChange={e => setForm({...form, name: e.target.value})}
          />
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-colors"
            placeholder="Email"
            type="email"
            value={form.email}
            onChange={e => setForm({...form, email: e.target.value})}
          />
          <input
            className="w-full bg-[#252525] border border-gray-700 p-3 rounded-xl text-white outline-none focus:border-orange-500 transition-colors"
            placeholder="Пароль"
            type="password"
            value={form.password}
            onChange={e => setForm({...form, password: e.target.value})}
          />
        </div>

        <div className="flex flex-col gap-3 mt-8">
          <button
            onClick={() => onSave(form)}
            disabled={loading || !form.email || !form.password}
            className="w-full bg-orange-500 hover:bg-orange-600 py-3 rounded-xl text-white font-bold disabled:opacity-50 transition-all"
          >
            {loading ? 'Создание...' : 'Создать'}
          </button>
          <button onClick={onClose} className="w-full text-gray-500 hover:text-white py-2 transition-colors">
            Отмена
          </button>
        </div>
      </div>
    </div>
  );
};
