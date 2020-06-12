#############
# TODO list:
##########################################################################################################
# 1. Main logic (biopython, flask, requests) - parse sequence / rEndonuclease -> return separated sequence
# Firstly, search through the rE list, suggest the matches, create complement only after separation
# 1.5 Database (PostgreSQL/MySQL): SQL script to UPDATE DB data with rEndonuclease list
# 2. Update main logic to suggest matching list of rEndonuclease (and separate after selection)
# 2.5 Unit tests (unittests / pytest)
# 3. FE part (HTML/CSS, Django, update logic to API-based, return rEndonuclease list to FE from DB)
# 3.5 Update FE (return suggested list, separation by selected item)
# 4.5 Update Unit tests
# 5. API / Selenium tests
# ---------------------------
# FE features:
# - Add new rEndonuclease through FE (save to DB directly)
# - Update visual part (separation)
# - TBD
##########################################################################################################