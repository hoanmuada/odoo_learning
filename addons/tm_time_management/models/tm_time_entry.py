# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TmTimeEntry(models.Model):
    _name = 'tm.time.entry'
    _description = 'Time Management Entry'
    _order = 'date desc, id desc'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(
        string='Description',
        required=True,
        tracking=True,
    )
    employee_id = fields.Many2one(
        'hr.employee',
        string='Employee',
        required=True,
        default=lambda self: self.env.user.employee_id,
        tracking=True,
    )
    user_id = fields.Many2one(
        'res.users',
        string='User',
        related='employee_id.user_id',
        store=True,
        readonly=True,
    )
    project_id = fields.Many2one(
        'project.project',
        string='Project',
        tracking=True,
    )
    task_id = fields.Many2one(
        'project.task',
        string='Task',
        domain="[('project_id', '=', project_id)]",
        tracking=True,
    )
    category_id = fields.Many2one(
        'tm.category',
        string='Category',
        tracking=True,
    )
    date = fields.Date(
        string='Date',
        required=True,
        default=fields.Date.context_today,
        tracking=True,
    )
    duration = fields.Float(
        string='Duration (Hours)',
        required=True,
        tracking=True,
        help='Time spent in hours (e.g. 1.5 = 1h30m)',
    )
    description = fields.Html(
        string='Notes',
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ], string='Status', default='draft', required=True, tracking=True)
    company_id = fields.Many2one(
        'res.company',
        string='Company',
        default=lambda self: self.env.company,
        required=True,
    )

    # -------------------------------------------------------------------------
    # CONSTRAINTS
    # -------------------------------------------------------------------------

    @api.constrains('duration')
    def _check_duration(self):
        for record in self:
            if record.duration <= 0:
                raise ValidationError('Duration must be greater than 0 hours.')
            if record.duration > 24:
                raise ValidationError('Duration cannot exceed 24 hours per entry.')

    # -------------------------------------------------------------------------
    # ONCHANGE
    # -------------------------------------------------------------------------

    @api.onchange('project_id')
    def _onchange_project_id(self):
        """Clear task when project changes."""
        if self.task_id and self.task_id.project_id != self.project_id:
            self.task_id = False

    # -------------------------------------------------------------------------
    # WORKFLOW ACTIONS
    # -------------------------------------------------------------------------

    def action_submit(self):
        """Submit entry for approval."""
        for record in self:
            if record.state != 'draft':
                raise ValidationError('Only draft entries can be submitted.')
            record.state = 'submitted'

    def action_approve(self):
        """Approve submitted entry (manager action)."""
        for record in self:
            if record.state != 'submitted':
                raise ValidationError('Only submitted entries can be approved.')
            record.state = 'approved'

    def action_reject(self):
        """Reject submitted entry (manager action)."""
        for record in self:
            if record.state != 'submitted':
                raise ValidationError('Only submitted entries can be rejected.')
            record.state = 'rejected'

    def action_reset_draft(self):
        """Reset entry to draft state."""
        for record in self:
            if record.state not in ('submitted', 'rejected'):
                raise ValidationError('Only submitted or rejected entries can be reset to draft.')
            record.state = 'draft'
