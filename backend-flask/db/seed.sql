INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('Karthik Muraliprasad', 'kmuralip@uci.edu', 'karthikmurali' ,'MOCK1'),
  ('Zeus Kart', 'zeuskart@gmail.com', 'zeuskart' ,'MOCK2');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'karthikmurali' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )
