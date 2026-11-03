from odoo import models
from odoo.tools import formatLang


class AccountJournal(models.Model):
    _inherit = 'account.journal'

    def _uses_default_account_as_outstanding(self):
        """True when this journal's Outstanding Receipts or Outstanding Payments
        account is set to the journal's own default account.

        In that setup account.payment._compute_reconciliation_status flags every
        payment as is_matched the moment it posts (see the
        "Allow user managing payments without any statement lines by using the
        bank account directly" branch), so current_statement_balance +
        direct_payments_balance only ever accumulates: it has no way to see the
        offsetting entry created when a bank statement line is later reconciled
        against that payment from another journal.
        """
        payment_method_lines = self.inbound_payment_method_line_ids | self.outbound_payment_method_line_ids
        return bool(payment_method_lines.filtered(
            lambda line: line.payment_account_id and line.payment_account_id == self.default_account_id
        ))

    def _get_gl_balance_formatted(self):
        self.ensure_one()
        gl_balance = sum(self.env['account.move.line'].search([
            ('account_id', '=', self.default_account_id.id),
            ('parent_state', '=', 'posted'),
        ]).mapped('balance'))
        currency = self.currency_id or self.company_id.sudo().currency_id
        return formatLang(self.env, gl_balance, currency_obj=currency)

    def _fill_bank_cash_dashboard_data(self, dashboard_data):
        # EXTENDS account
        # Fixes the "Balance" figure on the Accounting dashboard's journal card
        # for journals where the Outstanding account is the journal's own
        # default account (see _uses_default_account_as_outstanding).
        super()._fill_bank_cash_dashboard_data(dashboard_data)
        for journal in self.filtered(lambda j: j.type in ('bank', 'cash', 'credit')
                                     and j._uses_default_account_as_outstanding()):
            dashboard_data[journal.id]['account_balance'] = journal._get_gl_balance_formatted()

    def get_total_journal_amount(self):
        # EXTENDS account_accountant
        # Fixes the equivalent balance shown inside the bank reconciliation widget.
        if not (self.exists() and self._uses_default_account_as_outstanding()):
            return super().get_total_journal_amount()

        balance = ''
        if any(company in self.company_id._accessible_branches() for company in self.env.companies):
            balance = self._get_gl_balance_formatted()
        return {'balance_amount': balance, 'has_invalid_statements': self.has_invalid_statements}
