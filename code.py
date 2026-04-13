<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Advanced Banking System</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;600&family=Noto+Sans+Tamil:wght@400;600&display=swap');

  :root {
    --bg: #0a0e1a;
    --surface: #111827;
    --surface2: #1a2235;
    --border: #2a3450;
    --accent: #00d4aa;
    --accent2: #3b82f6;
    --danger: #ef4444;
    --warn: #f59e0b;
    --text: #e2e8f0;
    --muted: #64748b;
    --success: #10b981;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'IBM Plex Mono', 'Noto Sans Tamil', monospace;
    min-height: 100vh;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
  }

  .app-header {
    text-align: center;
    margin-bottom: 24px;
    padding: 20px;
  }

  .app-title {
    font-size: 22px;
    font-weight: 600;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
  }

  .app-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-top: 4px;
  }

  .lang-toggle {
    display: flex;
    gap: 8px;
    justify-content: center;
    margin-top: 12px;
  }

  .lang-btn {
    background: var(--surface2);
    border: 1px solid var(--border);
    color: var(--muted);
    padding: 6px 16px;
    border-radius: 20px;
    cursor: pointer;
    font-size: 12px;
    font-family: inherit;
    transition: all 0.2s;
  }

  .lang-btn.active {
    background: var(--accent);
    color: #0a0e1a;
    border-color: var(--accent);
    font-weight: 600;
  }

  .container {
    width: 100%;
    max-width: 900px;
    display: grid;
    grid-template-columns: 220px 1fr;
    gap: 16px;
  }

  .sidebar {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 16px 0;
    height: fit-content;
    position: sticky;
    top: 20px;
  }

  .sidebar-section {
    padding: 8px 16px 4px;
    font-size: 10px;
    color: var(--muted);
    letter-spacing: 1.5px;
    text-transform: uppercase;
  }

  .menu-item {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 10px 16px;
    cursor: pointer;
    font-size: 13px;
    color: var(--text);
    border-left: 3px solid transparent;
    transition: all 0.15s;
    font-family: inherit;
  }

  .menu-item:hover { background: var(--surface2); }

  .menu-item.active {
    background: var(--surface2);
    border-left-color: var(--accent);
    color: var(--accent);
  }

  .menu-icon { font-size: 14px; width: 18px; text-align: center; }

  .main-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 24px;
    min-height: 500px;
  }

  .panel-title {
    font-size: 16px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 1px solid var(--border);
    letter-spacing: 1px;
  }

  .form-group {
    margin-bottom: 16px;
  }

  label {
    display: block;
    font-size: 12px;
    color: var(--muted);
    margin-bottom: 6px;
    letter-spacing: 0.5px;
  }

  input[type="text"],
  input[type="number"],
  input[type="password"],
  input[type="datetime-local"],
  select {
    width: 100%;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 8px;
    color: var(--text);
    padding: 10px 14px;
    font-size: 14px;
    font-family: inherit;
    outline: none;
    transition: border-color 0.2s;
  }

  input:focus, select:focus {
    border-color: var(--accent);
  }

  .btn {
    padding: 10px 24px;
    border-radius: 8px;
    border: none;
    cursor: pointer;
    font-size: 14px;
    font-family: inherit;
    font-weight: 600;
    transition: all 0.15s;
    letter-spacing: 0.5px;
  }

  .btn-primary {
    background: var(--accent);
    color: #0a0e1a;
  }

  .btn-primary:hover { background: #00bfa0; }

  .btn-danger {
    background: var(--danger);
    color: white;
  }

  .btn-secondary {
    background: var(--surface2);
    color: var(--text);
    border: 1px solid var(--border);
  }

  .btn-secondary:hover { border-color: var(--accent); color: var(--accent); }

  .btn-sm { padding: 6px 14px; font-size: 12px; }

  .alert {
    padding: 12px 16px;
    border-radius: 8px;
    font-size: 13px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .alert-success { background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.4); color: var(--success); }
  .alert-error { background: rgba(239,68,68,0.15); border: 1px solid rgba(239,68,68,0.4); color: var(--danger); }
  .alert-info { background: rgba(59,130,246,0.15); border: 1px solid rgba(59,130,246,0.4); color: var(--accent2); }

  .card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 12px;
    margin-bottom: 20px;
  }

  .stat-card {
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 14px;
  }

  .stat-label { font-size: 11px; color: var(--muted); margin-bottom: 6px; }
  .stat-value { font-size: 20px; font-weight: 600; color: var(--accent); }

  .tx-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12px;
  }

  .tx-table th {
    padding: 8px 12px;
    text-align: left;
    color: var(--muted);
    border-bottom: 1px solid var(--border);
    font-weight: 400;
    letter-spacing: 0.5px;
  }

  .tx-table td {
    padding: 10px 12px;
    border-bottom: 1px solid rgba(42,52,80,0.5);
    color: var(--text);
  }

  .tx-table tr:last-child td { border-bottom: none; }
  .tx-table tr:hover td { background: var(--surface2); }

  .badge {
    display: inline-block;
    padding: 2px 8px;
    border-radius: 10px;
    font-size: 11px;
    font-weight: 600;
  }

  .badge-deposit { background: rgba(16,185,129,0.2); color: var(--success); }
  .badge-withdraw { background: rgba(239,68,68,0.2); color: var(--danger); }
  .badge-transfer { background: rgba(59,130,246,0.2); color: var(--accent2); }

  .balance-big {
    font-size: 36px;
    font-weight: 600;
    color: var(--accent);
    margin: 8px 0;
  }

  .account-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 16px;
    background: var(--surface2);
    border: 1px solid var(--border);
    border-radius: 10px;
    margin-bottom: 10px;
  }

  .account-info { flex: 1; }
  .account-num { font-size: 13px; font-weight: 600; color: var(--text); }
  .account-name { font-size: 12px; color: var(--muted); margin-top: 2px; }
  .account-bal { font-size: 16px; font-weight: 600; color: var(--accent); }

  .divider {
    height: 1px;
    background: var(--border);
    margin: 20px 0;
  }

  .two-col { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }

  .empty-state {
    text-align: center;
    padding: 40px 20px;
    color: var(--muted);
  }

  .empty-icon { font-size: 32px; margin-bottom: 12px; }
  .empty-text { font-size: 13px; }

  .modal-overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.7);
    z-index: 100;
    align-items: center;
    justify-content: center;
  }

  .modal-overlay.open { display: flex; }

  .modal {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 14px;
    padding: 28px;
    width: 100%;
    max-width: 420px;
    margin: 20px;
  }

  .modal-title {
    font-size: 15px;
    font-weight: 600;
    color: var(--accent);
    margin-bottom: 20px;
  }

  .modal-actions {
    display: flex;
    gap: 10px;
    justify-content: flex-end;
    margin-top: 20px;
  }

  .progress-bar {
    height: 4px;
    background: var(--border);
    border-radius: 2px;
    overflow: hidden;
    margin-top: 8px;
  }

  .progress-fill {
    height: 100%;
    background: var(--accent);
    transition: width 0.3s;
  }

  .scrollable { max-height: 320px; overflow-y: auto; }

  .scrollable::-webkit-scrollbar { width: 4px; }
  .scrollable::-webkit-scrollbar-track { background: var(--surface); }
  .scrollable::-webkit-scrollbar-thumb { background: var(--border); border-radius: 2px; }

  .section-header {
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 1px;
    text-transform: uppercase;
    margin-bottom: 12px;
  }

  .pin-dots {
    display: flex;
    gap: 8px;
    margin-top: 8px;
  }

  .pin-dot {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: var(--border);
    transition: background 0.1s;
  }

  .pin-dot.filled { background: var(--accent); }

  @media (max-width: 640px) {
    .container { grid-template-columns: 1fr; }
    .sidebar { position: static; }
    .two-col { grid-template-columns: 1fr; }
  }
</style>
</head>
<body>

<div class="app-header">
  <div class="app-title" id="appTitle">Advanced Banking System</div>
  <div class="app-subtitle" id="appSubtitle">Secure · Fast · Reliable</div>
  <div class="lang-toggle">
    <button class="lang-btn active" onclick="setLang('EN')">English</button>
    <button class="lang-btn" onclick="setLang('TA')">தமிழ்</button>
  </div>
</div>

<div class="container">
  <nav class="sidebar" id="sidebar"></nav>
  <main class="main-panel" id="mainPanel"></main>
</div>

<!-- PIN Modal -->
<div class="modal-overlay" id="pinModal">
  <div class="modal">
    <div class="modal-title" id="pinModalTitle">Enter PIN</div>
    <div class="form-group">
      <label id="pinModalLabel">PIN</label>
      <input type="password" id="pinInput" maxlength="8" placeholder="••••" inputmode="numeric" oninput="updatePinDots()"/>
      <div class="pin-dots" id="pinDots">
        <div class="pin-dot"></div>
        <div class="pin-dot"></div>
        <div class="pin-dot"></div>
        <div class="pin-dot"></div>
      </div>
    </div>
    <div id="pinError" class="alert alert-error" style="display:none"></div>
    <div class="modal-actions">
      <button class="btn btn-secondary" onclick="closePinModal()">Cancel</button>
      <button class="btn btn-primary" onclick="submitPin()">Confirm</button>
    </div>
  </div>
</div>

<!-- Dev Modal -->
<div class="modal-overlay" id="devModal">
  <div class="modal">
    <div class="modal-title" id="devModalTitle">Developer Access</div>
    <div class="form-group">
      <label>Developer Code</label>
      <input type="password" id="devCodeInput" placeholder="••••"/>
    </div>
    <div id="devError" class="alert alert-error" style="display:none"></div>
    <div class="modal-actions">
      <button class="btn btn-secondary" onclick="closeDevModal()">Cancel</button>
      <button class="btn btn-primary" onclick="submitDevCode()">Enter</button>
    </div>
  </div>
</div>

<script>
// ═══════════════════════════════════════════
//  LANGUAGE PACK
// ═══════════════════════════════════════════
const LANG = {
  EN: {
    appTitle: "Advanced Banking System",
    appSubtitle: "Secure · Fast · Reliable",
    nav_dashboard: "Dashboard",
    nav_create: "Create Account",
    nav_deposit: "Deposit",
    nav_withdraw: "Withdraw",
    nav_transfer: "Transfer",
    nav_balance: "View Balance",
    nav_history: "Transaction History",
    nav_scheduled: "Scheduled",
    nav_tools: "Balance Tools",
    nav_manage: "Account Settings",
    nav_developer: "Developer",
    section_banking: "BANKING",
    section_tools: "TOOLS",
    section_admin: "ADMIN",
    // Dashboard
    dash_title: "Dashboard",
    dash_accounts: "Total Accounts",
    dash_transactions: "Transactions",
    dash_scheduled: "Scheduled",
    dash_no_accounts: "No accounts yet. Create one to get started.",
    // Create Account
    create_title: "Create New Account",
    create_acc_no: "Account Number",
    create_name: "Full Name",
    create_initial_bal: "Initial Balance",
    create_pin: "PIN (4-8 digits)",
    create_btn: "Create Account",
    create_success: "Account created successfully!",
    create_exists: "Account number already exists.",
    create_invalid_pin: "PIN must be 4-8 digits.",
    create_fill: "Please fill all fields correctly.",
    // Deposit
    deposit_title: "Deposit Funds",
    dep_acc_no: "Account Number",
    dep_amount: "Amount",
    dep_btn: "Deposit",
    dep_success: "Deposit successful!",
    // Withdraw
    withdraw_title: "Withdraw Funds",
    wd_note: "Service fee: ₹1.00 per withdrawal",
    wd_btn: "Withdraw",
    wd_success: "Withdrawal successful!",
    wd_insufficient: "Insufficient funds (including ₹1.00 service fee).",
    // Transfer
    transfer_title: "Transfer Funds",
    tr_from: "From Account",
    tr_to: "To Account",
    tr_amount: "Amount",
    tr_note: "Service fee: ₹1.00 per transfer",
    tr_btn: "Transfer",
    tr_success: "Transfer successful!",
    tr_insufficient: "Insufficient funds (including ₹1.00 service fee).",
    tr_same: "Cannot transfer to the same account.",
    // Balance
    balance_title: "View Balance",
    bal_acc: "Account Number",
    bal_btn: "Check Balance",
    bal_label: "Current Balance",
    bal_created: "Account Created",
    bal_name: "Account Holder",
    // History
    history_title: "Transaction History",
    hist_acc: "Account Number",
    hist_btn: "Load History",
    hist_when: "Date & Time",
    hist_type: "Type",
    hist_from: "From",
    hist_to: "To",
    hist_amount: "Amount",
    hist_fee: "Fee",
    hist_none: "No transactions found.",
    // Scheduled
    sched_title: "Scheduled Transactions",
    sched_none: "No scheduled transactions.",
    sched_index: "#",
    sched_type: "Type",
    sched_from: "From",
    sched_to: "To",
    sched_amount: "Amount",
    sched_for: "Scheduled For",
    sched_cancel: "Cancel",
    sched_cancelled: "Scheduled transaction cancelled.",
    sched_add_title: "Schedule New Transaction",
    sched_type_label: "Transaction Type",
    sched_acc: "Account Number",
    sched_to_acc: "Destination Account",
    sched_amount_label: "Amount",
    sched_date: "Schedule Date & Time",
    sched_btn: "Schedule",
    sched_success: "Transaction scheduled!",
    sched_past: "Date must be in the future.",
    sched_fee_note: "Scheduling fee: ₹1.70 (service + SMS + processing)",
    // Balance Tools
    tools_title: "Balance Tools",
    bt_smart_title: "Smart Balance Calculator",
    bt_smart_acc: "Account Number",
    bt_smart_date: "Calculate up to date",
    bt_smart_btn: "Calculate",
    bt_current: "Current Balance",
    bt_sched_dep: "Scheduled Deposits",
    bt_sched_wd: "Scheduled Withdrawals",
    bt_predicted: "Predicted Balance",
    bt_predictor_title: "Balance Predictor (AI)",
    bt_predictor_btn: "Predict",
    bt_avg_dep: "Avg. Deposit",
    bt_avg_wd: "Avg. Withdrawal",
    bt_expected: "Expected Change",
    bt_confidence: "Confidence",
    // Settings
    settings_title: "Account Settings",
    set_summary_title: "Account Summary",
    set_change_pin: "Change PIN",
    set_new_pin: "New PIN",
    set_pin_btn: "Update PIN",
    set_pin_success: "PIN updated successfully!",
    set_delete: "Delete Account",
    set_delete_confirm: "Type DELETE to confirm account deletion:",
    set_delete_btn: "Delete Account",
    set_deleted: "Account deleted.",
    set_delete_aborted: "Type DELETE exactly to confirm.",
    // Developer
    dev_title: "Developer Options",
    dev_report_title: "System Report",
    dev_export_btn: "Export CSV",
    dev_reset_btn: "Reset All Data",
    dev_export_ok: "Data exported as CSV files.",
    dev_reset_confirm: "Type CONFIRM to reset all data:",
    dev_reset_ok: "All data cleared.",
    dev_reset_aborted: "Type CONFIRM exactly to proceed.",
    dev_all_accounts: "All Accounts",
    dev_acc_num: "Account No.",
    dev_acc_name: "Name",
    dev_acc_bal: "Balance",
    dev_acc_created: "Created",
    // Common
    acc_not_found: "Account not found.",
    invalid_amount: "Amount must be greater than zero.",
    invalid_input: "Invalid input.",
    enter_acc: "Account Number",
    pin_wrong: "Incorrect PIN.",
    loading: "Processing...",
    error: "Error",
    success: "Success",
    type_deposit: "DEPOSIT",
    type_withdraw: "WITHDRAW",
    type_transfer: "TRANSFER",
  },
  TA: {
    appTitle: "மேம்படுத்தப்பட்ட வங்கி அமைப்பு",
    appSubtitle: "பாதுகாப்பானது · வேகமானது · நம்பகமானது",
    nav_dashboard: "டாஷ்போர்டு",
    nav_create: "கணக்கு உருவாக்கு",
    nav_deposit: "பணம் செலுத்து",
    nav_withdraw: "பணம் எடு",
    nav_transfer: "பணம் மாற்று",
    nav_balance: "இருப்பு பார்",
    nav_history: "பரிமாற்ற வரலாறு",
    nav_scheduled: "திட்டமிட்டவை",
    nav_tools: "இருப்பு கருவிகள்",
    nav_manage: "கணக்கு அமைப்புகள்",
    nav_developer: "டெவலப்பர்",
    section_banking: "வங்கி சேவைகள்",
    section_tools: "கருவிகள்",
    section_admin: "நிர்வாகம்",
    // Dashboard
    dash_title: "டாஷ்போர்டு",
    dash_accounts: "மொத்த கணக்குகள்",
    dash_transactions: "பரிமாற்றங்கள்",
    dash_scheduled: "திட்டமிட்டவை",
    dash_no_accounts: "கணக்குகள் இல்லை. ஒன்றை உருவாக்கவும்.",
    // Create Account
    create_title: "புதிய கணக்கு உருவாக்கு",
    create_acc_no: "கணக்கு எண்",
    create_name: "முழு பெயர்",
    create_initial_bal: "ஆரம்ப இருப்பு",
    create_pin: "ஊ-குறி (4-8 இலக்கங்கள்)",
    create_btn: "கணக்கு உருவாக்கு",
    create_success: "கணக்கு வெற்றிகரமாக உருவாக்கப்பட்டது!",
    create_exists: "கணக்கு எண் ஏற்கனவே உள்ளது.",
    create_invalid_pin: "ஊ-குறி 4-8 இலக்கங்களாக இருக்க வேண்டும்.",
    create_fill: "அனைத்து புலங்களையும் சரியாக நிரப்பவும்.",
    // Deposit
    deposit_title: "பணம் செலுத்துதல்",
    dep_acc_no: "கணக்கு எண்",
    dep_amount: "தொகை",
    dep_btn: "செலுத்து",
    dep_success: "பணம் செலுத்துதல் வெற்றிகரமாக முடிந்தது!",
    // Withdraw
    withdraw_title: "பணம் எடுத்தல்",
    wd_note: "சேவை கட்டணம்: ₹1.00",
    wd_btn: "எடு",
    wd_success: "பணம் எடுத்தல் வெற்றிகரமாக முடிந்தது!",
    wd_insufficient: "போதுமான இருப்பு இல்லை (₹1.00 கட்டணம் உட்பட).",
    // Transfer
    transfer_title: "பணம் மாற்றுதல்",
    tr_from: "அனுப்புவோர் கணக்கு",
    tr_to: "பெறுவோர் கணக்கு",
    tr_amount: "தொகை",
    tr_note: "சேவை கட்டணம்: ₹1.00",
    tr_btn: "மாற்று",
    tr_success: "பணம் மாற்றுதல் வெற்றிகரமாக முடிந்தது!",
    tr_insufficient: "போதுமான இருப்பு இல்லை (₹1.00 கட்டணம் உட்பட).",
    tr_same: "ஒரே கணக்குக்கு மாற்ற முடியாது.",
    // Balance
    balance_title: "இருப்பு பார்க்கவும்",
    bal_acc: "கணக்கு எண்",
    bal_btn: "இருப்பு சரிபார்",
    bal_label: "தற்போதைய இருப்பு",
    bal_created: "கணக்கு உருவாக்கப்பட்ட தேதி",
    bal_name: "கணக்கு வைத்திருப்பவர்",
    // History
    history_title: "பரிமாற்ற வரலாறு",
    hist_acc: "கணக்கு எண்",
    hist_btn: "வரலாறு காட்டு",
    hist_when: "தேதி & நேரம்",
    hist_type: "வகை",
    hist_from: "அனுப்பியவர்",
    hist_to: "பெற்றவர்",
    hist_amount: "தொகை",
    hist_fee: "கட்டணம்",
    hist_none: "பரிமாற்றங்கள் இல்லை.",
    // Scheduled
    sched_title: "திட்டமிட்ட பரிமாற்றங்கள்",
    sched_none: "திட்டமிட்ட பரிமாற்றங்கள் இல்லை.",
    sched_index: "#",
    sched_type: "வகை",
    sched_from: "அனுப்பியவர்",
    sched_to: "பெறுவோர்",
    sched_amount: "தொகை",
    sched_for: "திட்டமிட்ட நேரம்",
    sched_cancel: "ரத்து",
    sched_cancelled: "திட்டமிட்ட பரிமாற்றம் ரத்து செய்யப்பட்டது.",
    sched_add_title: "புதிய பரிமாற்றம் திட்டமிடு",
    sched_type_label: "பரிமாற்ற வகை",
    sched_acc: "கணக்கு எண்",
    sched_to_acc: "இலக்கு கணக்கு",
    sched_amount_label: "தொகை",
    sched_date: "திட்டமிட்ட தேதி & நேரம்",
    sched_btn: "திட்டமிடு",
    sched_success: "பரிமாற்றம் திட்டமிடப்பட்டது!",
    sched_past: "தேதி எதிர்காலத்தில் இருக்க வேண்டும்.",
    sched_fee_note: "திட்டமிடல் கட்டணம்: ₹1.70",
    // Balance Tools
    tools_title: "இருப்பு கருவிகள்",
    bt_smart_title: "நுட்பமான இருப்பு கணக்கீடு",
    bt_smart_acc: "கணக்கு எண்",
    bt_smart_date: "இந்த தேதி வரை கணக்கிடு",
    bt_smart_btn: "கணக்கிடு",
    bt_current: "தற்போதைய இருப்பு",
    bt_sched_dep: "திட்டமிட்ட வரவுகள்",
    bt_sched_wd: "திட்டமிட்ட செலவுகள்",
    bt_predicted: "கணிக்கப்பட்ட இருப்பு",
    bt_predictor_title: "இருப்பு கணிப்பான் (AI)",
    bt_predictor_btn: "கணி",
    bt_avg_dep: "சராசரி வரவு",
    bt_avg_wd: "சராசரி செலவு",
    bt_expected: "எதிர்பார்க்கப்படும் மாற்றம்",
    bt_confidence: "நம்பிக்கை அளவு",
    // Settings
    settings_title: "கணக்கு அமைப்புகள்",
    set_summary_title: "கணக்கு சுருக்கம்",
    set_change_pin: "ஊ-குறி மாற்று",
    set_new_pin: "புதிய ஊ-குறி",
    set_pin_btn: "ஊ-குறி புதுப்பி",
    set_pin_success: "ஊ-குறி வெற்றிகரமாக புதுப்பிக்கப்பட்டது!",
    set_delete: "கணக்கு நீக்கு",
    set_delete_confirm: "உறுதிப்படுத்த DELETE என்று தட்டச்சு செய்யவும்:",
    set_delete_btn: "கணக்கு நீக்கு",
    set_deleted: "கணக்கு நீக்கப்பட்டது.",
    set_delete_aborted: "உறுதிப்படுத்த சரியாக DELETE என்று தட்டச்சு செய்யவும்.",
    // Developer
    dev_title: "டெவலப்பர் விருப்பங்கள்",
    dev_report_title: "அமைப்பு அறிக்கை",
    dev_export_btn: "CSV ஏற்றுமதி",
    dev_reset_btn: "அனைத்தையும் மீட்டமை",
    dev_export_ok: "தரவு CSV கோப்புகளாக ஏற்றுமதி செய்யப்பட்டது.",
    dev_reset_confirm: "அனைத்து தரவையும் மீட்டமைக்க CONFIRM என்று தட்டச்சு செய்யவும்:",
    dev_reset_ok: "அனைத்து தரவும் அழிக்கப்பட்டது.",
    dev_reset_aborted: "சரியாக CONFIRM என்று தட்டச்சு செய்யவும்.",
    dev_all_accounts: "அனைத்து கணக்குகள்",
    dev_acc_num: "கணக்கு எண்.",
    dev_acc_name: "பெயர்",
    dev_acc_bal: "இருப்பு",
    dev_acc_created: "உருவாக்கப்பட்டது",
    // Common
    acc_not_found: "கணக்கு கிடைக்கவில்லை.",
    invalid_amount: "தொகை பூஜ்யத்தை விட அதிகமாக இருக்க வேண்டும்.",
    invalid_input: "தவறான உள்ளீடு.",
    enter_acc: "கணக்கு எண்",
    pin_wrong: "தவறான ஊ-குறி.",
    loading: "செயலாக்குகிறது...",
    error: "பிழை",
    success: "வெற்றி",
    type_deposit: "வரவு",
    type_withdraw: "எடுத்தல்",
    type_transfer: "மாற்றல்",
  }
};

// ═══════════════════════════════════════════
//  STATE
// ═══════════════════════════════════════════
const STATE = {
  lang: 'EN',
  accounts: [],
  transactions: [],
  activePanel: 'dashboard',
  SERVICE_CHARGE: 1.00,
  SMS_COST: 0.50,
  PRE_SCHEDULE_COST: 0.20,
  DEV_CODE: '0000',
};

function t(key) {
  const l = LANG[STATE.lang] || LANG.EN;
  return l[key] !== undefined ? l[key] : (LANG.EN[key] || key);
}

// ═══════════════════════════════════════════
//  PERSISTENCE
// ═══════════════════════════════════════════
function saveData() {
  try {
    localStorage.setItem('banking_accounts', JSON.stringify(STATE.accounts));
    localStorage.setItem('banking_transactions', JSON.stringify(STATE.transactions));
  } catch(e) { /* fallback: no persistence in strict sandboxes */ }
}

function loadData() {
  try {
    const a = localStorage.getItem('banking_accounts');
    const tx = localStorage.getItem('banking_transactions');
    if (a) STATE.accounts = JSON.parse(a);
    if (tx) STATE.transactions = JSON.parse(tx);
  } catch(e) {}
}

// ═══════════════════════════════════════════
//  CRYPTO (SHA-256 polyfill using djb2 for browser compat)
// ═══════════════════════════════════════════
async function hashPin(pin) {
  if (window.crypto && window.crypto.subtle) {
    const enc = new TextEncoder();
    const buf = await window.crypto.subtle.digest('SHA-256', enc.encode(pin));
    return Array.from(new Uint8Array(buf)).map(b => b.toString(16).padStart(2,'0')).join('');
  }
  // fallback hash
  let h = 0;
  for (let i = 0; i < pin.length; i++) {
    h = Math.imul(31, h) + pin.charCodeAt(i) | 0;
  }
  return (h >>> 0).toString(16).padStart(8, '0');
}

// ═══════════════════════════════════════════
//  HELPERS
// ═══════════════════════════════════════════
function findAccount(accNo) {
  return STATE.accounts.findIndex(a => a.acc === accNo.trim());
}

function formatTime(ts) {
  if (!ts) return '-';
  const d = new Date(ts);
  return d.toLocaleString();
}

function formatAmt(n) {
  return '₹' + Number(n).toFixed(2);
}

function showAlert(container, msg, type='info') {
  const el = document.getElementById(container);
  if (!el) return;
  const icons = { success: '✓', error: '✗', info: 'ℹ' };
  el.innerHTML = `<div class="alert alert-${type}">${icons[type] || ''} ${msg}</div>`;
  setTimeout(() => { if (el) el.innerHTML = ''; }, 4000);
}

function txTypeBadge(type) {
  const map = {
    DEPOSIT: 'badge-deposit',
    WITHDRAW: 'badge-withdraw',
    TRANSFER: 'badge-transfer',
  };
  const label = t('type_' + type.toLowerCase()) || type;
  return `<span class="badge ${map[type] || ''}">${label}</span>`;
}

// ═══════════════════════════════════════════
//  PIN MODAL
// ═══════════════════════════════════════════
let pinResolve = null;

function updatePinDots() {
  const val = document.getElementById('pinInput').value;
  const dots = document.querySelectorAll('#pinDots .pin-dot');
  dots.forEach((d, i) => {
    d.classList.toggle('filled', i < val.length);
  });
}

function requestPin(title) {
  return new Promise(resolve => {
    pinResolve = resolve;
    document.getElementById('pinModalTitle').textContent = title || t('enter_acc');
    document.getElementById('pinInput').value = '';
    document.getElementById('pinError').style.display = 'none';
    updatePinDots();
    document.getElementById('pinModal').classList.add('open');
    setTimeout(() => document.getElementById('pinInput').focus(), 100);
  });
}

function closePinModal() {
  document.getElementById('pinModal').classList.remove('open');
  if (pinResolve) pinResolve(null);
  pinResolve = null;
}

function submitPin() {
  const val = document.getElementById('pinInput').value.trim();
  if (!val) return;
  document.getElementById('pinModal').classList.remove('open');
  if (pinResolve) pinResolve(val);
  pinResolve = null;
}

document.getElementById('pinInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') submitPin();
  if (e.key === 'Escape') closePinModal();
});

async function verifyPinForAccount(idx) {
  const pin = await requestPin('Enter PIN');
  if (!pin) return false;
  const hashed = await hashPin(pin);
  if (STATE.accounts[idx].pin_hash === hashed) return true;
  showNotification(t('pin_wrong'), 'error');
  return false;
}

// ═══════════════════════════════════════════
//  DEV MODAL
// ═══════════════════════════════════════════
let devResolve = null;

function openDevModal() {
  return new Promise(resolve => {
    devResolve = resolve;
    document.getElementById('devCodeInput').value = '';
    document.getElementById('devError').style.display = 'none';
    document.getElementById('devModal').classList.add('open');
    setTimeout(() => document.getElementById('devCodeInput').focus(), 100);
  });
}

function closeDevModal() {
  document.getElementById('devModal').classList.remove('open');
  if (devResolve) devResolve(false);
  devResolve = null;
}

function submitDevCode() {
  const val = document.getElementById('devCodeInput').value.trim();
  if (val === STATE.DEV_CODE) {
    document.getElementById('devModal').classList.remove('open');
    if (devResolve) devResolve(true);
    devResolve = null;
  } else {
    document.getElementById('devError').textContent = 'Access denied. Incorrect code.';
    document.getElementById('devError').style.display = 'flex';
  }
}

document.getElementById('devCodeInput').addEventListener('keydown', e => {
  if (e.key === 'Enter') submitDevCode();
});

// ═══════════════════════════════════════════
//  NOTIFICATION
// ═══════════════════════════════════════════
function showNotification(msg, type='success') {
  const n = document.createElement('div');
  n.className = `alert alert-${type}`;
  n.style.cssText = 'position:fixed;top:20px;right:20px;z-index:999;max-width:320px;animation:fadeIn 0.2s';
  n.textContent = msg;
  document.body.appendChild(n);
  setTimeout(() => n.remove(), 3000);
}

// ═══════════════════════════════════════════
//  SIDEBAR
// ═══════════════════════════════════════════
function renderSidebar() {
  const items = [
    { id: 'dashboard', icon: '◈', key: 'nav_dashboard', section: 'section_banking' },
    { id: 'create', icon: '+', key: 'nav_create' },
    { id: 'deposit', icon: '↓', key: 'nav_deposit' },
    { id: 'withdraw', icon: '↑', key: 'nav_withdraw' },
    { id: 'transfer', icon: '⇄', key: 'nav_transfer' },
    { id: 'balance', icon: '◉', key: 'nav_balance' },
    { id: 'history', icon: '≡', key: 'nav_history' },
    { id: 'scheduled', icon: '◷', key: 'nav_scheduled', section: 'section_tools' },
    { id: 'tools', icon: '⚙', key: 'nav_tools' },
    { id: 'manage', icon: '◈', key: 'nav_manage', section: 'section_admin' },
    { id: 'developer', icon: '</>', key: 'nav_developer' },
  ];

  let html = '';
  let lastSection = '';
  items.forEach(item => {
    if (item.section) {
      html += `<div class="sidebar-section">${t(item.section)}</div>`;
    }
    html += `<div class="menu-item ${STATE.activePanel === item.id ? 'active' : ''}" onclick="navigate('${item.id}')">
      <span class="menu-icon">${item.icon}</span>
      <span>${t(item.key)}</span>
    </div>`;
  });
  document.getElementById('sidebar').innerHTML = html;
}

function navigate(panel) {
  STATE.activePanel = panel;
  renderSidebar();
  renderPanel();
}

// ═══════════════════════════════════════════
//  PANELS
// ═══════════════════════════════════════════
function renderPanel() {
  const panels = {
    dashboard, create, deposit, withdraw, transfer,
    balance, history, scheduled, tools, manage, developer
  };
  const fn = panels[STATE.activePanel];
  if (fn) document.getElementById('mainPanel').innerHTML = fn();
  else document.getElementById('mainPanel').innerHTML = '<div class="empty-state">Panel not found</div>';
}

// ─── DASHBOARD ───
function dashboard() {
  const totalBal = STATE.accounts.reduce((s, a) => s + a.bal, 0);
  const pending = STATE.transactions.filter(tx => tx.is_scheduled).length;

  let recentTx = '';
  const recent = [...STATE.transactions].reverse().slice(0, 5);
  if (recent.length > 0) {
    recentTx = `<div class="section-header" style="margin-top:20px">Recent Transactions</div>
    <div class="scrollable"><table class="tx-table">
      <thead><tr>
        <th>${t('hist_when')}</th><th>${t('hist_type')}</th>
        <th>${t('hist_from')}</th><th>${t('hist_amount')}</th>
      </tr></thead><tbody>
      ${recent.map(tx => `<tr>
        <td style="font-size:11px;color:var(--muted)">${formatTime(tx.when)}</td>
        <td>${txTypeBadge(tx.type)}</td>
        <td>${tx.from}</td>
        <td style="color:var(--accent)">${formatAmt(tx.amount)}</td>
      </tr>`).join('')}
    </tbody></table></div>`;
  }

  let accountList = '';
  if (STATE.accounts.length === 0) {
    accountList = `<div class="empty-state"><div class="empty-icon">◈</div><div class="empty-text">${t('dash_no_accounts')}</div></div>`;
  } else {
    accountList = STATE.accounts.map(a =>
      `<div class="account-row">
        <div class="account-info">
          <div class="account-num">${a.acc}</div>
          <div class="account-name">${a.name}</div>
        </div>
        <div class="account-bal">${formatAmt(a.bal)}</div>
      </div>`
    ).join('');
  }

  return `<div class="panel-title">${t('dash_title')}</div>
    <div class="card-grid">
      <div class="stat-card">
        <div class="stat-label">${t('dash_accounts')}</div>
        <div class="stat-value">${STATE.accounts.length}</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">${t('dash_transactions')}</div>
        <div class="stat-value">${STATE.transactions.length}</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">${t('dash_scheduled')}</div>
        <div class="stat-value">${pending}</div>
      </div>
      <div class="stat-card">
        <div class="stat-label">Total Balance</div>
        <div class="stat-value" style="font-size:16px">${formatAmt(totalBal)}</div>
      </div>
    </div>
    ${accountList}
    ${recentTx}`;
}

// ─── CREATE ───
function create() {
  return `<div class="panel-title">${t('create_title')}</div>
    <div id="createAlert"></div>
    <div class="form-group">
      <label>${t('create_acc_no')}</label>
      <input type="text" id="c_acc" placeholder="e.g. ACC001"/>
    </div>
    <div class="form-group">
      <label>${t('create_name')}</label>
      <input type="text" id="c_name" placeholder="e.g. Kumar"/>
    </div>
    <div class="two-col">
      <div class="form-group">
        <label>${t('create_initial_bal')}</label>
        <input type="number" id="c_bal" min="0" step="0.01" placeholder="0.00"/>
      </div>
      <div class="form-group">
        <label>${t('create_pin')}</label>
        <input type="password" id="c_pin" maxlength="8" inputmode="numeric" placeholder="••••"/>
      </div>
    </div>
    <button class="btn btn-primary" onclick="doCreate()">${t('create_btn')}</button>`;
}

async function doCreate() {
  const acc = document.getElementById('c_acc').value.trim();
  const name = document.getElementById('c_name').value.trim();
  const balRaw = document.getElementById('c_bal').value;
  const pin = document.getElementById('c_pin').value.trim();
  const bal = parseFloat(balRaw);

  if (!acc || !name || isNaN(bal) || bal < 0 || !pin) {
    showAlert('createAlert', t('create_fill'), 'error'); return;
  }
  if (!pin.match(/^\d{4,8}$/)) {
    showAlert('createAlert', t('create_invalid_pin'), 'error'); return;
  }
  if (findAccount(acc) !== -1) {
    showAlert('createAlert', t('create_exists'), 'error'); return;
  }
  const pin_hash = await hashPin(pin);
  STATE.accounts.push({ acc, name, bal: Math.round(bal * 100) / 100, pin_hash, created: Date.now() });
  saveData();
  showAlert('createAlert', t('create_success'), 'success');
  document.getElementById('c_acc').value = '';
  document.getElementById('c_name').value = '';
  document.getElementById('c_bal').value = '';
  document.getElementById('c_pin').value = '';
}

// ─── DEPOSIT ───
function deposit() {
  return `<div class="panel-title">${t('deposit_title')}</div>
    <div id="depAlert"></div>
    <div class="form-group">
      <label>${t('dep_acc_no')}</label>
      <input type="text" id="dep_acc" placeholder="Account number"/>
    </div>
    <div class="form-group">
      <label>${t('dep_amount')}</label>
      <input type="number" id="dep_amt" min="0.01" step="0.01" placeholder="0.00"/>
    </div>
    <button class="btn btn-primary" onclick="doDeposit()">${t('dep_btn')}</button>`;
}

async function doDeposit() {
  const accNo = document.getElementById('dep_acc').value.trim();
  const amt = parseFloat(document.getElementById('dep_amt').value);
  if (!accNo) { showAlert('depAlert', t('invalid_input'), 'error'); return; }
  if (isNaN(amt) || amt <= 0) { showAlert('depAlert', t('invalid_amount'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('depAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('depAlert', t('pin_wrong'), 'error'); return; }
  STATE.accounts[idx].bal = Math.round((STATE.accounts[idx].bal + amt) * 100) / 100;
  STATE.transactions.push({ when: Date.now(), type: 'DEPOSIT', from: accNo, to: accNo, amount: Math.round(amt*100)/100, fee: 0, is_scheduled: false, scheduled_for: 0 });
  saveData();
  showAlert('depAlert', t('dep_success'), 'success');
  document.getElementById('dep_amt').value = '';
}

// ─── WITHDRAW ───
function withdraw() {
  return `<div class="panel-title">${t('withdraw_title')}</div>
    <div class="alert alert-info" style="margin-bottom:16px">ℹ ${t('wd_note')}</div>
    <div id="wdAlert"></div>
    <div class="form-group">
      <label>${t('enter_acc')}</label>
      <input type="text" id="wd_acc" placeholder="Account number"/>
    </div>
    <div class="form-group">
      <label>${t('dep_amount')}</label>
      <input type="number" id="wd_amt" min="0.01" step="0.01" placeholder="0.00"/>
    </div>
    <button class="btn btn-primary" onclick="doWithdraw()">${t('wd_btn')}</button>`;
}

async function doWithdraw() {
  const accNo = document.getElementById('wd_acc').value.trim();
  const amt = parseFloat(document.getElementById('wd_amt').value);
  if (!accNo) { showAlert('wdAlert', t('invalid_input'), 'error'); return; }
  if (isNaN(amt) || amt <= 0) { showAlert('wdAlert', t('invalid_amount'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('wdAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('wdAlert', t('pin_wrong'), 'error'); return; }
  const total = Math.round((amt + STATE.SERVICE_CHARGE) * 100) / 100;
  if (STATE.accounts[idx].bal < total) { showAlert('wdAlert', t('wd_insufficient'), 'error'); return; }
  STATE.accounts[idx].bal = Math.round((STATE.accounts[idx].bal - total) * 100) / 100;
  STATE.transactions.push({ when: Date.now(), type: 'WITHDRAW', from: accNo, to: '-', amount: Math.round(amt*100)/100, fee: STATE.SERVICE_CHARGE, is_scheduled: false, scheduled_for: 0 });
  saveData();
  showAlert('wdAlert', t('wd_success'), 'success');
  document.getElementById('wd_amt').value = '';
}

// ─── TRANSFER ───
function transfer() {
  return `<div class="panel-title">${t('transfer_title')}</div>
    <div class="alert alert-info" style="margin-bottom:16px">ℹ ${t('tr_note')}</div>
    <div id="trAlert"></div>
    <div class="two-col">
      <div class="form-group">
        <label>${t('tr_from')}</label>
        <input type="text" id="tr_from" placeholder="From account"/>
      </div>
      <div class="form-group">
        <label>${t('tr_to')}</label>
        <input type="text" id="tr_to" placeholder="To account"/>
      </div>
    </div>
    <div class="form-group">
      <label>${t('tr_amount')}</label>
      <input type="number" id="tr_amt" min="0.01" step="0.01" placeholder="0.00"/>
    </div>
    <button class="btn btn-primary" onclick="doTransfer()">${t('tr_btn')}</button>`;
}

async function doTransfer() {
  const fromNo = document.getElementById('tr_from').value.trim();
  const toNo = document.getElementById('tr_to').value.trim();
  const amt = parseFloat(document.getElementById('tr_amt').value);
  if (!fromNo || !toNo) { showAlert('trAlert', t('invalid_input'), 'error'); return; }
  if (fromNo === toNo) { showAlert('trAlert', t('tr_same'), 'error'); return; }
  if (isNaN(amt) || amt <= 0) { showAlert('trAlert', t('invalid_amount'), 'error'); return; }
  const idxFrom = findAccount(fromNo);
  if (idxFrom === -1) { showAlert('trAlert', t('acc_not_found') + ' (From)', 'error'); return; }
  const idxTo = findAccount(toNo);
  if (idxTo === -1) { showAlert('trAlert', t('acc_not_found') + ' (To)', 'error'); return; }
  const ok = await verifyPinForAccount(idxFrom);
  if (!ok) { showAlert('trAlert', t('pin_wrong'), 'error'); return; }
  const total = Math.round((amt + STATE.SERVICE_CHARGE) * 100) / 100;
  if (STATE.accounts[idxFrom].bal < total) { showAlert('trAlert', t('tr_insufficient'), 'error'); return; }
  STATE.accounts[idxFrom].bal = Math.round((STATE.accounts[idxFrom].bal - total) * 100) / 100;
  STATE.accounts[idxTo].bal = Math.round((STATE.accounts[idxTo].bal + amt) * 100) / 100;
  STATE.transactions.push({ when: Date.now(), type: 'TRANSFER', from: fromNo, to: toNo, amount: Math.round(amt*100)/100, fee: STATE.SERVICE_CHARGE, is_scheduled: false, scheduled_for: 0 });
  saveData();
  showAlert('trAlert', t('tr_success'), 'success');
  document.getElementById('tr_amt').value = '';
}

// ─── BALANCE ───
function balance() {
  return `<div class="panel-title">${t('balance_title')}</div>
    <div id="balAlert"></div>
    <div class="form-group">
      <label>${t('bal_acc')}</label>
      <input type="text" id="bal_acc" placeholder="Account number"/>
    </div>
    <button class="btn btn-primary" onclick="doBalance()">${t('bal_btn')}</button>
    <div id="balResult"></div>`;
}

async function doBalance() {
  const accNo = document.getElementById('bal_acc').value.trim();
  if (!accNo) { showAlert('balAlert', t('invalid_input'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('balAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('balAlert', t('pin_wrong'), 'error'); return; }
  const acc = STATE.accounts[idx];
  document.getElementById('balResult').innerHTML = `
    <div class="divider"></div>
    <div class="account-row" style="flex-direction:column;align-items:flex-start;gap:12px">
      <div>
        <div class="stat-label">${t('bal_name')}</div>
        <div style="font-size:16px;font-weight:600;margin-top:4px">${acc.name}</div>
      </div>
      <div>
        <div class="stat-label">${t('bal_label')}</div>
        <div class="balance-big">${formatAmt(acc.bal)}</div>
      </div>
      <div>
        <div class="stat-label">${t('bal_created')}</div>
        <div style="font-size:12px;color:var(--muted)">${formatTime(acc.created)}</div>
      </div>
    </div>`;
}

// ─── HISTORY ───
function history() {
  return `<div class="panel-title">${t('history_title')}</div>
    <div id="histAlert"></div>
    <div style="display:flex;gap:10px;margin-bottom:16px">
      <input type="text" id="hist_acc" placeholder="Account number" style="flex:1"/>
      <button class="btn btn-primary" onclick="doHistory()">${t('hist_btn')}</button>
    </div>
    <div id="histResult"></div>`;
}

function doHistory() {
  const accNo = document.getElementById('hist_acc').value.trim();
  if (!accNo) { showAlert('histAlert', t('invalid_input'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('histAlert', t('acc_not_found'), 'error'); return; }
  const txs = STATE.transactions.filter(tx => tx.from === accNo || tx.to === accNo);
  if (txs.length === 0) {
    document.getElementById('histResult').innerHTML = `<div class="empty-state"><div class="empty-text">${t('hist_none')}</div></div>`;
    return;
  }
  document.getElementById('histResult').innerHTML = `
    <div class="scrollable"><table class="tx-table">
      <thead><tr>
        <th>${t('hist_when')}</th><th>${t('hist_type')}</th>
        <th>${t('hist_from')}</th><th>${t('hist_to')}</th>
        <th>${t('hist_amount')}</th><th>${t('hist_fee')}</th>
      </tr></thead>
      <tbody>${[...txs].reverse().map(tx => `<tr>
        <td style="font-size:11px;white-space:nowrap">${formatTime(tx.when)}</td>
        <td>${txTypeBadge(tx.type)}</td>
        <td>${tx.from}</td><td>${tx.to}</td>
        <td style="color:var(--accent)">${formatAmt(tx.amount)}</td>
        <td style="color:var(--muted)">${formatAmt(tx.fee)}</td>
      </tr>`).join('')}</tbody>
    </table></div>`;
}

// ─── SCHEDULED ───
function scheduled() {
  const schTxs = STATE.transactions
    .map((tx, i) => ({ ...tx, _idx: i }))
    .filter(tx => tx.is_scheduled);

  let list = '';
  if (schTxs.length === 0) {
    list = `<div class="empty-state"><div class="empty-text">${t('sched_none')}</div></div>`;
  } else {
    list = `<div class="scrollable"><table class="tx-table">
      <thead><tr>
        <th>#</th><th>${t('sched_type')}</th><th>${t('sched_from')}</th>
        <th>${t('sched_to')}</th><th>${t('sched_amount')}</th>
        <th>${t('sched_for')}</th><th></th>
      </tr></thead>
      <tbody>${schTxs.map((tx, i) => `<tr>
        <td style="color:var(--muted)">${i+1}</td>
        <td>${txTypeBadge(tx.type)}</td>
        <td>${tx.from}</td><td>${tx.to||'-'}</td>
        <td style="color:var(--accent)">${formatAmt(tx.amount)}</td>
        <td style="font-size:11px">${formatTime(tx.scheduled_for)}</td>
        <td><button class="btn btn-danger btn-sm" onclick="cancelScheduled(${tx._idx})">${t('sched_cancel')}</button></td>
      </tr>`).join('')}</tbody>
    </table></div>`;
  }

  return `<div class="panel-title">${t('sched_title')}</div>
    <div id="schedAlert"></div>
    ${list}
    <div class="divider"></div>
    <div class="section-header">${t('sched_add_title')}</div>
    <div class="alert alert-info" style="margin-bottom:16px">ℹ ${t('sched_fee_note')}</div>
    <div class="form-group">
      <label>${t('sched_type_label')}</label>
      <select id="sch_type" onchange="renderSchedToField()">
        <option value="deposit">Deposit</option>
        <option value="withdraw">Withdraw</option>
        <option value="transfer">Transfer</option>
      </select>
    </div>
    <div class="two-col">
      <div class="form-group">
        <label>${t('sched_acc')}</label>
        <input type="text" id="sch_acc" placeholder="Account number"/>
      </div>
      <div id="sch_to_field"></div>
    </div>
    <div class="two-col">
      <div class="form-group">
        <label>${t('sched_amount_label')}</label>
        <input type="number" id="sch_amt" min="0.01" step="0.01" placeholder="0.00"/>
      </div>
      <div class="form-group">
        <label>${t('sched_date')}</label>
        <input type="datetime-local" id="sch_date"/>
      </div>
    </div>
    <button class="btn btn-primary" onclick="doSchedule()">${t('sched_btn')}</button>`;
}

function renderSchedToField() {
  const type = document.getElementById('sch_type')?.value;
  const el = document.getElementById('sch_to_field');
  if (!el) return;
  if (type === 'transfer') {
    el.innerHTML = `<div class="form-group"><label>${t('sched_to_acc')}</label><input type="text" id="sch_to" placeholder="Destination account"/></div>`;
  } else {
    el.innerHTML = '';
  }
}

async function cancelScheduled(idx) {
  if (idx < 0 || idx >= STATE.transactions.length) return;
  STATE.transactions[idx].is_scheduled = false;
  STATE.transactions[idx].scheduled_for = 0;
  saveData();
  showNotification(t('sched_cancelled'), 'success');
  navigate('scheduled');
}

async function doSchedule() {
  const type = document.getElementById('sch_type').value;
  const accNo = document.getElementById('sch_acc').value.trim();
  const amt = parseFloat(document.getElementById('sch_amt').value);
  const dateVal = document.getElementById('sch_date').value;

  if (!accNo || isNaN(amt) || amt <= 0 || !dateVal) {
    showAlert('schedAlert', t('invalid_input'), 'error'); return;
  }
  const ts = new Date(dateVal).getTime();
  if (ts <= Date.now()) { showAlert('schedAlert', t('sched_past'), 'error'); return; }

  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('schedAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('schedAlert', t('pin_wrong'), 'error'); return; }

  let toNo = '';
  if (type === 'transfer') {
    const toEl = document.getElementById('sch_to');
    if (!toEl) { showAlert('schedAlert', t('invalid_input'), 'error'); return; }
    toNo = toEl.value.trim();
    if (!toNo || findAccount(toNo) === -1) {
      showAlert('schedAlert', t('acc_not_found') + ' (To)', 'error'); return;
    }
  }

  const fee = Math.round((STATE.SERVICE_CHARGE + STATE.SMS_COST + STATE.PRE_SCHEDULE_COST) * 100) / 100;
  STATE.transactions.push({
    when: Date.now(), type: type.toUpperCase(),
    from: accNo, to: toNo, amount: Math.round(amt*100)/100,
    fee, is_scheduled: true, scheduled_for: ts
  });
  saveData();
  showAlert('schedAlert', t('sched_success'), 'success');
  setTimeout(() => navigate('scheduled'), 1500);
}

// ─── BALANCE TOOLS ───
function tools() {
  return `<div class="panel-title">${t('tools_title')}</div>
    <div class="section-header">${t('bt_smart_title')}</div>
    <div id="smartAlert"></div>
    <div class="two-col">
      <div class="form-group">
        <label>${t('bt_smart_acc')}</label>
        <input type="text" id="bt_acc" placeholder="Account number"/>
      </div>
      <div class="form-group">
        <label>${t('bt_smart_date')}</label>
        <input type="datetime-local" id="bt_date"/>
      </div>
    </div>
    <button class="btn btn-primary" onclick="doSmartCalc()" style="margin-bottom:20px">${t('bt_smart_btn')}</button>
    <div id="smartResult"></div>
    <div class="divider"></div>
    <div class="section-header">${t('bt_predictor_title')}</div>
    <div id="predAlert"></div>
    <div class="form-group">
      <label>${t('bt_smart_acc')}</label>
      <input type="text" id="pred_acc" placeholder="Account number"/>
    </div>
    <button class="btn btn-primary" onclick="doPredictor()">${t('bt_predictor_btn')}</button>
    <div id="predResult"></div>`;
}

async function doSmartCalc() {
  const accNo = document.getElementById('bt_acc').value.trim();
  const dateVal = document.getElementById('bt_date').value;
  if (!accNo || !dateVal) { showAlert('smartAlert', t('invalid_input'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('smartAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('smartAlert', t('pin_wrong'), 'error'); return; }
  const target = new Date(dateVal).getTime();
  const current = STATE.accounts[idx].bal;
  const schedDep = STATE.transactions
    .filter(tx => tx.is_scheduled && tx.scheduled_for <= target && tx.to === accNo && ['DEPOSIT','TRANSFER'].includes(tx.type))
    .reduce((s, tx) => s + tx.amount, 0);
  const schedWd = STATE.transactions
    .filter(tx => tx.is_scheduled && tx.scheduled_for <= target && tx.from === accNo && ['WITHDRAW','TRANSFER'].includes(tx.type))
    .reduce((s, tx) => s + tx.amount + tx.fee, 0);
  const predicted = Math.round((current + schedDep - schedWd) * 100) / 100;
  const pct = Math.max(0, Math.min(100, Math.round(predicted / Math.max(current, 1) * 100)));
  document.getElementById('smartResult').innerHTML = `
    <div class="card-grid" style="margin-top:12px">
      <div class="stat-card"><div class="stat-label">${t('bt_current')}</div><div class="stat-value" style="font-size:16px">${formatAmt(current)}</div></div>
      <div class="stat-card"><div class="stat-label">${t('bt_sched_dep')}</div><div class="stat-value" style="font-size:16px;color:var(--success)">+${formatAmt(schedDep)}</div></div>
      <div class="stat-card"><div class="stat-label">${t('bt_sched_wd')}</div><div class="stat-value" style="font-size:16px;color:var(--danger)">-${formatAmt(schedWd)}</div></div>
      <div class="stat-card"><div class="stat-label">${t('bt_predicted')}</div><div class="stat-value">${formatAmt(predicted)}</div></div>
    </div>`;
}

async function doPredictor() {
  const accNo = document.getElementById('pred_acc').value.trim();
  if (!accNo) { showAlert('predAlert', t('invalid_input'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('predAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('predAlert', t('pin_wrong'), 'error'); return; }
  const completed = STATE.transactions.filter(tx => !tx.is_scheduled);
  const depAmts = completed.filter(tx => (tx.type === 'DEPOSIT' && tx.to === accNo) || (tx.type === 'TRANSFER' && tx.to === accNo)).map(tx => tx.amount);
  const wdAmts  = completed.filter(tx => tx.from === accNo && ['WITHDRAW','TRANSFER'].includes(tx.type)).map(tx => tx.amount);
  const avgDep = depAmts.length > 0 ? depAmts.reduce((s,v) => s+v, 0) / depAmts.length : 0;
  const avgWd  = wdAmts.length  > 0 ? wdAmts.reduce((s,v)  => s+v, 0) / wdAmts.length  : 0;
  const expected = Math.round((avgDep - avgWd) * 0.7 * 100) / 100;
  const predicted = Math.round((STATE.accounts[idx].bal + expected) * 100) / 100;
  const total = depAmts.length + wdAmts.length;
  const conf = total >= 20 ? 85 : total >= 5 ? 65 : 40;
  document.getElementById('predResult').innerHTML = `
    <div class="card-grid" style="margin-top:12px">
      <div class="stat-card"><div class="stat-label">${t('bt_avg_dep')} (n=${depAmts.length})</div><div class="stat-value" style="font-size:16px;color:var(--success)">${formatAmt(avgDep)}</div></div>
      <div class="stat-card"><div class="stat-label">${t('bt_avg_wd')} (n=${wdAmts.length})</div><div class="stat-value" style="font-size:16px;color:var(--danger)">${formatAmt(avgWd)}</div></div>
      <div class="stat-card"><div class="stat-label">${t('bt_expected')}</div><div class="stat-value" style="font-size:16px">${expected >= 0 ? '+' : ''}${formatAmt(expected)}</div></div>
      <div class="stat-card"><div class="stat-label">${t('bt_predicted')}</div><div class="stat-value">${formatAmt(predicted)}</div></div>
    </div>
    <div class="stat-card" style="margin-top:12px">
      <div class="stat-label">${t('bt_confidence')}</div>
      <div style="font-size:20px;font-weight:600;color:var(--accent);margin:6px 0">${conf}%</div>
      <div class="progress-bar"><div class="progress-fill" style="width:${conf}%"></div></div>
    </div>`;
}

// ─── ACCOUNT SETTINGS ───
function manage() {
  return `<div class="panel-title">${t('settings_title')}</div>
    <div id="manageAlert"></div>
    <div class="form-group">
      <label>${t('enter_acc')}</label>
      <input type="text" id="mg_acc" placeholder="Account number" oninput="loadSummary()"/>
    </div>
    <div id="summaryBox"></div>
    <div class="divider"></div>
    <div class="section-header">${t('set_change_pin')}</div>
    <div class="two-col">
      <div class="form-group">
        <label>${t('set_new_pin')}</label>
        <input type="password" id="mg_new_pin" maxlength="8" inputmode="numeric" placeholder="New PIN"/>
      </div>
      <div style="display:flex;align-items:flex-end;padding-bottom:16px">
        <button class="btn btn-primary" onclick="doChangePin()">${t('set_pin_btn')}</button>
      </div>
    </div>
    <div class="divider"></div>
    <div class="section-header" style="color:var(--danger)">${t('set_delete')}</div>
    <div class="form-group">
      <label>${t('set_delete_confirm')}</label>
      <input type="text" id="mg_delete_confirm" placeholder="DELETE"/>
    </div>
    <button class="btn btn-danger" onclick="doDeleteAccount()">${t('set_delete_btn')}</button>`;
}

function loadSummary() {
  const accNo = document.getElementById('mg_acc')?.value.trim();
  if (!accNo) return;
  const idx = findAccount(accNo);
  const el = document.getElementById('summaryBox');
  if (!el) return;
  if (idx === -1) { el.innerHTML = ''; return; }
  const acc = STATE.accounts[idx];
  const txCount = STATE.transactions.filter(tx => tx.from === acc.acc || tx.to === acc.acc).length;
  el.innerHTML = `<div class="account-row" style="flex-direction:column;align-items:flex-start;gap:8px;margin-bottom:8px">
    <div style="display:flex;justify-content:space-between;width:100%">
      <span style="color:var(--muted);font-size:12px">${acc.acc}</span>
      <span class="balance-big" style="font-size:20px">${formatAmt(acc.bal)}</span>
    </div>
    <div style="font-size:14px;font-weight:600">${acc.name}</div>
    <div style="font-size:11px;color:var(--muted)">${txCount} transactions · Created ${formatTime(acc.created)}</div>
  </div>`;
}

async function doChangePin() {
  const accNo = document.getElementById('mg_acc').value.trim();
  const newPin = document.getElementById('mg_new_pin').value.trim();
  if (!accNo) { showAlert('manageAlert', t('invalid_input'), 'error'); return; }
  if (!newPin.match(/^\d{4,8}$/)) { showAlert('manageAlert', t('create_invalid_pin'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('manageAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('manageAlert', t('pin_wrong'), 'error'); return; }
  STATE.accounts[idx].pin_hash = await hashPin(newPin);
  saveData();
  showAlert('manageAlert', t('set_pin_success'), 'success');
  document.getElementById('mg_new_pin').value = '';
}

async function doDeleteAccount() {
  const accNo = document.getElementById('mg_acc').value.trim();
  const confirm = document.getElementById('mg_delete_confirm').value.trim();
  if (confirm !== 'DELETE') { showAlert('manageAlert', t('set_delete_aborted'), 'error'); return; }
  const idx = findAccount(accNo);
  if (idx === -1) { showAlert('manageAlert', t('acc_not_found'), 'error'); return; }
  const ok = await verifyPinForAccount(idx);
  if (!ok) { showAlert('manageAlert', t('pin_wrong'), 'error'); return; }
  STATE.accounts.splice(idx, 1);
  STATE.transactions.forEach(tx => {
    if (tx.from === accNo) tx.from = '[deleted]';
    if (tx.to === accNo) tx.to = '[deleted]';
  });
  saveData();
  showAlert('manageAlert', t('set_deleted'), 'success');
  document.getElementById('mg_acc').value = '';
  document.getElementById('mg_delete_confirm').value = '';
  document.getElementById('summaryBox').innerHTML = '';
}

// ─── DEVELOPER ───
function developer() {
  return `<div class="panel-title">${t('dev_title')}</div>
    <div id="devPanelAlert"></div>
    <div class="alert alert-info" style="margin-bottom:16px">ℹ Developer code required to access.</div>
    <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px">
      <button class="btn btn-secondary" onclick="devExport()">${t('dev_export_btn')}</button>
      <button class="btn btn-secondary" onclick="devReport()">${t('dev_report_title')}</button>
      <button class="btn btn-danger" onclick="devReset()">${t('dev_reset_btn')}</button>
    </div>
    <div id="devContent"></div>`;
}

async function devExport() {
  const ok = await openDevModal();
  if (!ok) return;
  let csv1 = 'acc,name,balance,created\n';
  STATE.accounts.forEach(a => {
    csv1 += `${a.acc},${a.name},${a.bal.toFixed(2)},${formatTime(a.created)}\n`;
  });
  let csv2 = 'when,type,from,to,amount,fee,scheduled\n';
  STATE.transactions.forEach(tx => {
    csv2 += `${formatTime(tx.when)},${tx.type},${tx.from},${tx.to},${tx.amount},${tx.fee},${tx.is_scheduled}\n`;
  });
  [['accounts_export.csv', csv1], ['transactions_export.csv', csv2]].forEach(([name, data]) => {
    const a = document.createElement('a');
    a.href = 'data:text/csv;charset=utf-8,' + encodeURIComponent(data);
    a.download = name;
    a.click();
  });
  showAlert('devPanelAlert', t('dev_export_ok'), 'success');
}

async function devReport() {
  const ok = await openDevModal();
  if (!ok) return;
  const totalDep = STATE.transactions.filter(tx => tx.type==='DEPOSIT').reduce((s,tx)=>s+tx.amount,0);
  const totalWd  = STATE.transactions.filter(tx => tx.type==='WITHDRAW').reduce((s,tx)=>s+tx.amount,0);
  const totalTr  = STATE.transactions.filter(tx => tx.type==='TRANSFER').reduce((s,tx)=>s+tx.amount,0);
  const pending  = STATE.transactions.filter(tx => tx.is_scheduled).length;
  document.getElementById('devContent').innerHTML = `
    <div class="card-grid">
      <div class="stat-card"><div class="stat-label">Total Accounts</div><div class="stat-value">${STATE.accounts.length}</div></div>
      <div class="stat-card"><div class="stat-label">Transactions</div><div class="stat-value">${STATE.transactions.length}</div></div>
      <div class="stat-card"><div class="stat-label">Pending Scheduled</div><div class="stat-value">${pending}</div></div>
    </div>
    <div class="card-grid" style="margin-top:12px">
      <div class="stat-card"><div class="stat-label">Total Deposits</div><div class="stat-value" style="font-size:16px;color:var(--success)">${formatAmt(totalDep)}</div></div>
      <div class="stat-card"><div class="stat-label">Total Withdrawals</div><div class="stat-value" style="font-size:16px;color:var(--danger)">${formatAmt(totalWd)}</div></div>
      <div class="stat-card"><div class="stat-label">Total Transfers</div><div class="stat-value" style="font-size:16px">${formatAmt(totalTr)}</div></div>
    </div>
    <div class="divider"></div>
    <div class="section-header">${t('dev_all_accounts')}</div>
    <div class="scrollable"><table class="tx-table">
      <thead><tr>
        <th>${t('dev_acc_num')}</th><th>${t('dev_acc_name')}</th>
        <th>${t('dev_acc_bal')}</th><th>${t('dev_acc_created')}</th>
      </tr></thead>
      <tbody>${STATE.accounts.map(a => `<tr>
        <td>${a.acc}</td><td>${a.name}</td>
        <td style="color:var(--accent)">${formatAmt(a.bal)}</td>
        <td style="font-size:11px;color:var(--muted)">${formatTime(a.created)}</td>
      </tr>`).join('')}</tbody>
    </table></div>`;
}

async function devReset() {
  const ok = await openDevModal();
  if (!ok) return;
  const confirm = prompt(t('dev_reset_confirm'));
  if (confirm !== 'CONFIRM') { showAlert('devPanelAlert', t('dev_reset_aborted'), 'error'); return; }
  STATE.accounts = [];
  STATE.transactions = [];
  saveData();
  showAlert('devPanelAlert', t('dev_reset_ok'), 'success');
  document.getElementById('devContent').innerHTML = '';
}

// ═══════════════════════════════════════════
//  LANGUAGE
// ═══════════════════════════════════════════
function setLang(lang) {
  STATE.lang = lang;
  document.querySelectorAll('.lang-btn').forEach(b => {
    b.classList.toggle('active', b.textContent.includes(lang === 'EN' ? 'English' : 'தமிழ்'));
  });
  document.getElementById('appTitle').textContent = t('appTitle');
  document.getElementById('appSubtitle').textContent = t('appSubtitle');
  renderSidebar();
  renderPanel();
}

// ═══════════════════════════════════════════
//  INIT
// ═══════════════════════════════════════════
loadData();
renderSidebar();
renderPanel();
</script>
</body>
</html>
