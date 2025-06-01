from supabase import create_client, Client

url = "https://ofujwkootxpmztkktwte.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Im9mdWp3a29vdHhwbXp0a2t0d3RlIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDg3ODczMjUsImV4cCI6MjA2NDM2MzMyNX0.nE10ykXJKH3ceH5Vo5oTqE9HI7-6biy1DWBmm4cAE0A"

supabase: Client = create_client(url, key)
